# Project: 0x02. Minimum Operations


### Minimum Operations to Generate H Characters

In a text file, there is a single character H.
Your text editor can execute only two operations in this file: Copy All and Paste.
Given a number n, the task is to write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.


**Returns:**  
An integer representing the fewest number of operations needed.  
If n is impossible to achieve, return 0.

## Example

```python
n = 9

# Steps:
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
result = minOperations(n)  # Output: 6
```

In the given example, it takes 6 operations to generate 9 H characters in the file.

## Tasks

| Task                  | File                                       |
|-----------------------|--------------------------------------------|
| 0. Minimum Operations | [0-minoperations.py](./0-minoperations.py) |
