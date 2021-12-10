from typing import List


def find_by(key, val, collection):
    for item in collection:
        if item[key] == val:
            return item
