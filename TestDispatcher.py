# encoding: utf-8

import sys
import robot
import logging
import glob
import os
import shutil
import json
import gizeh
import moviepy.editor as mpy


from moviepy.video.VideoClip import ImageClip, VideoClip
from moviepy.video.tools.drawing import circle

import utilities
from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip


def main():

    if len(sys.argv) < 2:
        logging.error("No arguments given")

    # Remove old clips or blacklist them (if they are for example opened by some application)
    old_clips = []
    folder = 'RecordedClips'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            old_clips.append(file_path)

    # Remove old overlays (TODO: very similar to previous procedure, make a subroutine?)
    folder = 'Overlays'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            pass

    # Clear old recordings or create the recording file
    with open("NarrationRecord.json", "w") as file:
        initialization = []
        json.dump(initialization, file)

    for i in range(1, len(sys.argv)):
        print('Executing', sys.argv[i])
        try:
            robot.run(sys.argv[i], log='NONE', report='NONE', output='NONE', outputdir='RecordedClips')
        except Exception:
            print("Aborting testing")

    old_clips = []

    # Put newly recorded clips together in the order of creation
    clips = list(filter(os.path.isfile, glob.glob("RecordedClips/*.webm")))
    utilities.remove_blacklisted(clips, old_clips)
    clips.sort(key=lambda x: os.path.getmtime(x))

    # Convert filepaths to moviepy clips and get accurate durations of each test case
    segment_durations = []
    for i in range(len(clips)):
        clips[i] = VideoFileClip(clips[i])
        segment_durations.append(clips[i].duration)

    video = concatenate_videoclips(clips)
    video.write_videofile("Results/RawVideo.mp4")

    clips = [video]

    # Add highlighting of html elements using coordinates
    element_highlights = utilities.json_to_elementlocations_and_timestamps(segment_durations)
    resolution = utilities.get_resolution()
    i = 0
    for el in element_highlights:
        i = i+1
        dimensions = utilities.coordinates_to_dimensions(el["coordinates"])
        center = utilities.coordinates_to_center(el["coordinates"])
        surface = gizeh.Surface(width=resolution.width, height=resolution.height)
        shape = gizeh.rectangle(lx=dimensions["width"], ly=dimensions["height"], stroke_width=3, stroke=(1, 0, 0), xy=[center["x"], center["y"]])
        shape.draw(surface)
        surface.get_npimage()
        surface.write_to_png("Overlays/rectangle_" + str(i) + ".png")

    # Get newly created overlays
    overlays = list(filter(os.path.isfile, glob.glob("Overlays/*.png")))

    i = 0
    while i < len(element_highlights):
        img_clip = ImageClip(overlays[i]).set_start(element_highlights[i]["time"]).set_duration(2)
        clips.append(img_clip)
        i = i+1


    # Get font size based on screen resolution
    font_size = utilities.get_appropriate_font_size()

    # Add titles
    titles = utilities.json_to_testcase_names_and_timestamps(segment_durations)

    for title in titles:
        title_clip = TextClip(title["name"], font='Carlito-Bold', fontsize=(font_size*1.1), color='white',
                              stroke_color='black',  stroke_width=2)
        title_clip = title_clip.set_position("center").set_duration(2.5).set_start(title["time"]).crossfadein(0.1).crossfadeout(0.25)
        clips.append(title_clip)

    # Add subtitles
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=(font_size*0.9), color='white', bg_color='gray38')
    moviepy_subtitles = utilities.json_to_subtitles(segment_durations)
    subtitles = SubtitlesClip(moviepy_subtitles, generator).set_position(('center', 'bottom')).set_opacity(0.9)

    clips.append(subtitles)

    # Composite subtitles with the raw video
    result = CompositeVideoClip(clips)
    result.write_videofile("Results/HardCodedSubtitles.mp4", fps=video.fps, codec="libx264")

    # Add subtitles to /Results folder
    utilities.write_list_to_file(moviepy_subtitles, "Results/MoviePySubtitles.txt")

    # Add timestamps to /Results folder
    timestamps = utilities.json_to_timestamps(segment_durations)
    utilities.write_list_to_file(timestamps, "Results/Timestamps.txt")


def test_all(directory):
    """ Dispatch all tests in a directory. """
    raise NotImplementedError


def _dispatch_tests(tests):
    """ Dispatch all tests. """
    raise NotImplementedError


if __name__ == "__main__":
    main()
