# encoding: utf-8
import json
import pyautogui
import math
import time

def remove_blacklisted(target_list, blacklist):
    for element in blacklist:
        try:
            while True:
                target_list.remove(element)
                print(element + " will be excluded.")
        except ValueError:
            pass
    return target_list


def insert_to_list(target, insert, index):
    """Inserts a list to the indexed position of another list"""
    beginning = target[0:index]
    end = target[index:len(target)]
    return beginning + insert + end


def break_word(word, length):
    """Chops a word to smaller chunks with the maximum size of length"""
    return [word[i:i + length] for i in range(0, len(word), length)]


def start_times_2_cumulative_times(beginning_times):
    """
    Sum up all the durations in the back. For example:
    [29.9, 15.26, 11.73] -> [0, 29.9, 45.15]
    """
    cumulative_times = [0] * len(beginning_times)
    for i in range(0, len(beginning_times)):
        summed_time = 0
        for j in reversed(range(0, i)):
            summed_time += beginning_times[j]
        cumulative_times[i] = summed_time
    return cumulative_times


def json_to_subtitles(start_times):
    """
    Gets the subtitle data from NarrationRecord file
    :param beginning_times: duration of each section (video file length)
    :return: subtitles in moviyPy format:
             [((3.01, 7.01), 'This is a subtitle text.'), ...]
    """
    test_start = start_times_2_cumulative_times(start_times)
    subtitles = []
    test_index = 0
    with open("NarrationRecord.json", "r") as file:
        data = json.load(file)
        for suite in data:
            for test in suite["tests"]:
                for record in test["records"]:
                    if record["type"] != "narration":
                        continue
                    message = record["message"]
                    time = test_start[test_index] + record["time"]
                    endtime = time + subtitle_duration(message)
                    subtitles.append(((time, endtime), message))
                test_index += 1
    return subtitles


def json_to_elementlocations_and_timestamps(start_times):
    test_start = start_times_2_cumulative_times(start_times)
    coordinates = []
    test_index = 0
    with open("NarrationRecord.json", "r") as file:
        data = json.load(file)
        for suite in data:
            for test in suite["tests"]:
                for record in test["records"]:
                    if record["type"] != "element":
                        continue
                    time = test_start[test_index] + record["time"]
                    coordinates.append({"coordinates": record["coordinates"], "time": time})
                test_index += 1
    return coordinates


def json_to_timestamps(start_times):
    timestamps = start_times_2_cumulative_times(start_times)
    test_index = 0
    result = []
    with open("NarrationRecord.json", "r") as file:
        data = json.load(file)
        for suite in data:
            for test in suite["tests"]:
                timestamp = time.strftime('%M:%S', time.gmtime(timestamps[test_index]))
                result.append("%s: %s"%(timestamp, test["name"]))
                test_index += 1
    return result


def json_to_testcase_names_and_timestamps(start_times):
    timestamps = start_times_2_cumulative_times(start_times)
    names = []
    test_index = 0
    with open("NarrationRecord.json", "r") as file:
        data = json.load(file)
        for suite in data:
            for test in suite["tests"]:
                names.append({"name": test["name"], "time": timestamps[test_index]})
                test_index += 1
    return names


def add_linebreaks(text, max_length=40):
    """Adds linebreaks to subtitles"""
    # Break words that are over the maximum length to maximum length sized chunks
    """words = text.split()
    index = 0
    while index < len(words):
        if len(words[index]) > max_length:
            parts = break_word(words[index], max_length)
            words.pop(index)
            words = insert_to_list(words, parts, index)
        index += 1
    # Add linebreaks"""
    raise NotImplementedError


def write_list_to_file(given_list, filepath):
    with open(filepath, "w") as file:
        for element in given_list:
            file.write(str(element) + "\n")


def break_word(word, length):
    [word[i:i + length] for i in range(0, len(word), length)]


def insert_to_list(original_list, insert, index):
    beginning = original_list[0:index]
    end = original_list[index:len(original_list)]
    return beginning + insert + end



def subtitle_duration(str, min_duration=3):
    """Return either the minimum value or 20 characters per second
    """
    return max(min_duration, math.floor(len(str)/20))

def get_appropriate_font_size():
    """Calculates appropriate subtitle font based on monitor 1 resolution"""
    width = pyautogui.size().width
    return (math.floor((width)/25))
