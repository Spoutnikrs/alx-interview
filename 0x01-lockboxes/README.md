# Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may
contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

## Requirements

Your task is to implement a Python method `canUnlockAll(boxes)` which checks whether all boxes can be unlocked.

### Prototype

```python
def canUnlockAll(boxes):
    pass
```

- `boxes` is a list of lists.
- A key with the same number as a box opens that box.
- All keys are positive integers.
- There can be keys that do not have corresponding boxes.
- The first box `boxes[0]` is initially unlocked.
- The method should return `True` if all boxes can be opened, otherwise `False`.

## Example Usage

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Tasks

| Task         | File                               |
|--------------|------------------------------------|
| 0. Lockboxes | [0-lockboxes.py](./0-lockboxes.py) |
