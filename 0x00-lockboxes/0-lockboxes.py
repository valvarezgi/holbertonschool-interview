#!/usr/bin/python3
"""Lockboxes
"""


def canUnlockAll(boxes):
    """ Determines is all boxes can be opened
    Args:
        boxes (list): list of boxes (list)
    Return: True if all boxes can be opened, else return False
    """
    # Checks if boxes are a list
    if type(boxes) is not list or not all(type(box) is list for box in boxes):
        return False
    # Checks if boxes are empty
    if len(boxes) == 0:
        return False
    # Checks if there is only one box
    if len(boxes) == 1:
        return True
    # Checks if the first box is empty
    if not boxes[0] and len(boxes) > 1:
        return False
    # Dictionary of all boxes
    unlock = {k: False for k in range(len(boxes))}
    # unlock first box
    unlock[0] = True
    # List of all key's for first box
    keys = [key for key in boxes[0]]
    # Unlock boxes
    while keys:
        new_k = []
        for key in keys:
            if key in unlock.keys() and unlock[key] is False:
                new_k += boxes[key]
                unlock[key] = True
 
        if all(unlock.values()) and len(unlock) == len(boxes):
            return True
        # Verify new keys
        keys = new_k
    return False
