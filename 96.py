import numpy as np
import time


def read_sudoku(filename):
    f = open(filename, "r")
    sudoku_array = []
    for _ in range(50):
        f.readline()
        sudoku = []
        for _ in range(9):
            row = []
            row[:0] = f.readline().strip()
            sudoku.append([int(r) for r in row])
        sudoku_array.append(np.array(sudoku))
    return sudoku_array


def get_row_possibilities(r, sudoku):
    s = set(range(1,10))
    for j in range(9):
        s.discard(sudoku[r][j])
    return s


def get_column_possibilities(c, sudoku):
    s = set(range(1,10))
    for i in range(9):
        s.discard(sudoku[i][c])
    return s


def get_sq_possibilities(r, c, sudoku):
    s = set(range(1,10))
    row_start, col_start = r - r % 3, c - c % 3
    # print(r, row_start, c, col_start)
    for i in range(3):
        for j in range(3):
            s.discard(sudoku[row_start + i][col_start + j])
    return s


def find_unassigned(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return (-1, -1)


def backtrack(sudoku):
    i, j = find_unassigned(sudoku)
    if i == -1:
        return True

    r_set = get_row_possibilities(i, sudoku)
    c_set = get_column_possibilities(j, sudoku)
    s_set = get_sq_possibilities(i, j, sudoku)
    all_possibilities = r_set & c_set & s_set

    for elt in all_possibilities:
        sudoku[i][j] = elt
        if backtrack(sudoku):
            return True
        sudoku[i][j] = 0

    return False


if __name__ == "__main__":
    sudoku_array = read_sudoku("p096_sudoku.txt")

    t_sum = 0

    for i, sudoku in enumerate(sudoku_array):
        print(i, backtrack(sudoku))
        print(sudoku)
        t_sum += (100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2])
        print("t_sum", t_sum)