# N Queens Puzzle

## Project Overview

The N Queens puzzle is a classic problem in computer science and mathematics. The challenge is to place N non-attacking queens on an N×N chessboard. This project aims to implement a Python program that solves the N Queens problem using a backtracking algorithm.

### Usage

```bash
$ ./0-nqueens.py N
```

Where `N` is the size of the chessboard (N×N). The program will find and print every possible solution to the N Queens problem for the given value of `N`.

### Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```bash
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### Requirements

- Python 3
- Only the `sys` module is allowed for import

### Error Handling

The program handles the following errors:
- If the user provides an incorrect number of arguments, it prints:
  ```
  Usage: nqueens N
  ```
- If `N` is not an integer:
  ```
  N must be a number
  ```
- If `N` is smaller than 4:
  ```
  N must be at least 4
  ```

### Implementation

The solution uses a backtracking algorithm to explore all possible placements of queens on the board. For each solution, the program prints a list of coordinates for the queen placements where each coordinate is represented as `[row, column]`.

### How to Run

```bash
chmod +x 0-nqueens.py
./0-nqueens.py N
```

Replace `N` with the size of the board (4 or greater).
 provides a clear overview of the project, instructions on how to use the program, error handling, and implementation details. Let me know if you'd like to make any changes!