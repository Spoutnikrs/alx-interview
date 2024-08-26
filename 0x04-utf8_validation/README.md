# UTF-8 Validation

This project involves writing a method that determines if a given data set represents a valid UTF-8 encoding.

## Task Description

The goal is to implement a function that checks whether a sequence of integers represents valid UTF-8 encoded data. Each
integer in the data list represents one byte (8 bits).

### Prototype

```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data set, where each integer is one byte (8 bits).

    Returns:
        bool: True if the data set is a valid UTF-8 encoding, otherwise False.
    """
```

### Requirements

- A character in UTF-8 can be between 1 to 4 bytes long.
- The data set can contain multiple characters.
- Each integer in the data set represents one byte of data.
- Only the 8 least significant bits of each integer should be considered.

### Example

Consider the following test cases:

```python
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

### How to Test

You can test the function by creating a file called `0-main.py` with the following contents:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
```

Then, run the file:

```bash
$ ./0-main.py
True
True
False
```

