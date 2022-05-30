# encoding: utf-8

import sys
import robot
import logging
import glob
import os
import shutil
import json
import utilities
from moviepy.editor import VideoFileClip, concatenate_videoclips


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

    print(segment_durations)

    video = concatenate_videoclips(clips)
    video.write_videofile("RawVideo.mp4")


def test_all(directory):
    """ Dispatch all tests in a directory. """
    raise NotImplementedError


def _dispatch_tests(tests):
    """ Dispatch all tests. """
    raise NotImplementedError


if __name__ == "__main__":
    main()
