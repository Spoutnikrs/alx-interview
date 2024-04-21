#!/usr/bin/python3
def canUnlockAll(boxes):
    """Defines a function that determines if a box containing a list of lists can be opened using keys """
    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes)) # True
#
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes)) # True
#
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes)) # False
