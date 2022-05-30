# encoding: utf-8

import utilities
import json
from datetime import datetime


class NarrationRecorder(object):

    def __init__(self, test_suite):
        self.__start_time = None
        self.__test_data = None
        self.__suite_name = test_suite
        self.__add_suite_if_missing()

    def initialize_test_narration(self, test_name):
        self.__test_data = {"name": test_name, "records": []}
        self.__start_time = datetime.now()

    def add_narration(self, message):
        self.__test_data["records"].append({"type": "narration", "time": datetime.now(), "message": message})

    def append_to_json(self):
        # TODO: Remove later, this is just to compare the recorded duration vs the video file duration
        self.__test_data["duration"] = (datetime.now() - self.__start_time).total_seconds()

        self.__datetimes_to_elapsed_times()
        with open("NarrationRecord.json", "r") as file:
            data = json.load(file)
        with open("NarrationRecord.json", "w") as file:
            for item in data:
                if item.get("suite") == self.__suite_name:
                    item.get("tests").append(self.__test_data)
                    json.dump(data, file)
                    return

    def __datetimes_to_elapsed_times(self):
        records = self.__test_data.get("records")
        for r in records:
            timedelta = (r.get("time") - self.__start_time)
            r.update({"time": timedelta.total_seconds()})

    # TODO: Could be used in Suite Setup of .robot instead of current implementation
    #       where __init__ is run once by the suite and each time a new test case is executed
    #       and the awkward __create_suite_if_missing method is required
    """def register__suite(self):
        with open("NarrationRecord.json", "r") as file:
            data = json.load(file)
        with open("NarrationRecord.json", "w") as file:
            data.append({"suite": self.__suite_name, "tests": []})
            json.dump(data, file)"""

    def __add_suite_if_missing(self):
        with open("NarrationRecord.json", "r") as file:
            data = json.load(file)
        try:
            for item in data:
                if item.get("suite") == self.__suite_name:
                    return
        except KeyError:
            pass
        with open("NarrationRecord.json", "w") as file:
            data.append({"suite": self.__suite_name, "tests": []})
            json.dump(data, file)
