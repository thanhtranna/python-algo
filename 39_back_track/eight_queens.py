#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Board size
BOARD_SIZE = 8

solution_count = 0
queen_list = [0] * BOARD_SIZE


def eight_queens(cur_column: int):
    """
    Output all eight queen sequences that meet the requirements
    Use an array of length 8 to represent the column of the chessboard, and the number of the array is the row number of the queen on the current column
    :return:
    """
    if cur_column >= BOARD_SIZE:
        global solution_count
        solution_count += 1
        # solution
        print(queen_list)
    else:
        for i in range(BOARD_SIZE):
            if is_valid_pos(cur_column, i):
                queen_list[cur_column] = i
                eight_queens(cur_column + 1)


def is_valid_pos(cur_column: int, pos: int) -> bool:
    """
    Because the approach is to place 1 queen in each column
    So you don’t need to check the legitimacy of the column when checking, just check the row and the diagonal
    1. Row: Check whether the element of the array before the index of cur_column already exists pos
    2. Diagonal: Check the element of the array before the subscript cur_column, and the row spacing pos-QUEEN_LIST[i]
        And column spacing cur_column-whether i is consistent
    :param cur_column:
    :param pos:
    :return:
    """
    i = 0
    while i < cur_column:
        # Accompany
        if queen_list[i] == pos:
            return False
        # diagonal
        if cur_column - i == abs(pos - queen_list[i]):
            return False
        i += 1
    return True


if __name__ == '__main__':
    print('--- eight queens sequence ---')
    eight_queens(0)

    print('\n--- solution count ---')
    print(solution_count)
