# encoding: utf-8

import sys
import robot
import logging
import glob
import os
import shutil
import json
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

    # Add highlighting of html elements using coordinates

    # Get font size based on screen resolution
    font_size = utilities.get_appropriate_font_size()

    # Add titles
    titles = utilities.json_to_testcase_names_and_timestamps(segment_durations)
    clips = [video]
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
