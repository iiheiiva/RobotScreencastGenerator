# encoding: utf-8

def remove_blacklisted(target_list, blacklist):
    for element in blacklist:
        try:
            while True:
                target_list.remove(element)
                print(element + " will be excluded.")
        except ValueError:
            pass
    return target_list
