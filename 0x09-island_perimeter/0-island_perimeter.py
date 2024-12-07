#!/usr/bin/python3
"""
docs
"""


def island_perimeter(grid):
    """
    docs
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Add 4 for each land cell initially
                perimeter += 4

                # Check the cell above
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check the cell to the left
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
