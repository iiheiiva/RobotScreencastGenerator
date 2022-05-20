# encoding: utf-8

import sys
import robot
import logging
import os
import shutil
import json
import datetime


def main():
    if len(sys.argv) < 2:
        logging.error("No arguments given")

    # Remove old clips
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


def test_all(directory):
    """ Dispatch all tests in a directory. """
    raise NotImplementedError


def _dispatch_tests(tests):
    """ Dispatch all tests. """
    raise NotImplementedError


if __name__ == "__main__":
    main()
