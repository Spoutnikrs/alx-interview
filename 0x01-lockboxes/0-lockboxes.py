#!/usr/bin/python3
def canUnlockAll(boxes):
    """Defines a function that determines if a box containing a list of lists can be opened using keys """
    unlocked_boxes = [0]  # Box 0 is already unlocked
    keys = list(boxes[0])  # Start with keys from Box 0

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            keys.extend(boxes[key])  # newly opened box keys

    return len(unlocked_boxes) == len(boxes)

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes)) # True
#
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes)) # True
#
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes)) # False
