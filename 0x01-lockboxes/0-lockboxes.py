#!/usr/bin/env python3
"""0-lockboxes.py"""


def canUnlockAll(boxes):
    """
    determine if all boxes can be opened
    """
    number_boxes = len(boxes)
    unlocked_boxes = set([0])
    available_keys = boxes[0]

    while available_keys:
        new_keys = []
        for key in available_keys:
            if key < number_boxes and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                new_keys.extend(boxes[key])
        available_keys = new_keys
    return len(unlocked_boxes) == number_boxes
