"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with
numbers in such a way that each column, each row, and each of the nine 3 × 3
sub-grids that compose the grid all contain all of the numbers from 1 to 9 one
time.

Implement an algorithm that will check whether the given grid of numbers
represents a valid Sudoku puzzle according to the layout rules described
above. Note that the puzzle represented by grid does not have to be solvable.

=== Example ===

for:
    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

the output should be:
    sudoku2(grid) = true

for:
    grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
            ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
            ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
            ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
            ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
            ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
            ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

the output should be:
    sudoku2(grid) = true
"""

def is_correct_inner_grids(x, y, grid) -> bool:
    a = [grid[i][j] for i in range(x, x+3)
                    for j in range(y, y+3)
                    if grid[i][j] != '.']

    b = set([grid[i][j] for i in range(x, x+3)
                        for j in range(y, y+3)
                        if grid[i][j] != '.'])

    return len(a) == len(b)


def is_correct_lines_columns(i, grid) -> bool:
    a = set(j for j in grid[i] if j != '.')
    b = [j for j in grid[i] if j != '.']

    c = set([grid[x][i] for x in range(9) if grid[x][i] != '.'])
    d = [grid[x][i] for x in range(9) if grid[x][i] != '.']

    return len(a) == len(b) and len(c) == len(d)


def sudoku2(grid) -> bool:
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_correct_inner_grids(i, j, grid):
                return False

    for i in range(9):
        if not is_correct_lines_columns(i, grid):
            return False
    return True



if __name__ == '__main__':
    # tests
    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

    print(sudoku2(grid)) # true

    grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
            ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
            ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
            ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
            ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
            ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
            ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

    print(sudoku2(grid)) # false
