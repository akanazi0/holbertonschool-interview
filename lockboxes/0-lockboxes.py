#!/usr/bin/python3
"""Module for canUnlockAll method."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list of list of int): List representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = {0}
    keys_stack = [0]

    while keys_stack:
        current_box = keys_stack.pop()

        for key in boxes[current_box]:
            if key < n and key not in opened:
                opened.add(key)
                keys_stack.append(key)
                if len(opened) == n:
                    return True

    return len(opened) == n
