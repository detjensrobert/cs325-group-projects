"""
    This file contains the template for Assignment3.  For testing it, I will
    place it in a different directory, call the function <vidrach_itky_leda>,
    and check its output. So, you can add/remove  whatever you want to/from
    this file.  But, don't change the name of the file or the name/signature
    of the following function.

    Also, I will use <python3> to run this code.
"""

import numpy  # for better matrix printing


def vidrach_itky_leda(input_file_path, output_file_path):
    """
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    """

    infile = open(input_file_path, mode="r")
    outfile = open(output_file_path, mode="w")

    board_size = int(infile.readline())

    board = infile.readlines()
    # split lines into each space & convert to ints
    board = [list(map(int, line.strip().split(","))) for line in board]

    red_pos = (0, 0)
    blue_pos = (board_size - 1, board_size - 1)
    history = {}  # memoization state tracker, keyed by (red_pos, blue_pos)

    print(f"Board size: {board_size}x{board_size}")
    print(numpy.matrix(board))

    moves = calculate_best_move(board, red_pos, blue_pos, history)

    outfile.write(str(moves))
    infile.close()
    outfile.close()
    return moves


def calculate_best_move(board, red_pos, blue_pos, history):
    """
    Returns the minimum number of moves needed to solve VIL.
    Works recursively and (hopefully) memoizes as to not be awful.
    """

    print(f"Checking r:{red_pos} b:{blue_pos}")

    move_results = []

    # ===================
    # check red positions
    # ===================

    if red_pos != (
        len(board) - 1,
        len(board) - 1,
    ):  # if red has made it, no need to move it anymore
        move_dist = board[red_pos[0]][red_pos[1]]

        # up
        new_pos = (red_pos[0], red_pos[1] - move_dist)
        if new_pos[1] >= 0 and new_pos != blue_pos:
            move_results.append(calc_move(board, new_pos, blue_pos, history))

        # down
        new_pos = (red_pos[0], red_pos[1] + move_dist)
        if new_pos[1] < len(board) and new_pos != blue_pos:
            move_results.append(calc_move(board, new_pos, blue_pos, history))

        # left
        new_pos = (red_pos[0] - move_dist, red_pos[1])
        if new_pos[0] >= 0 and new_pos != blue_pos:
            move_results.append(calc_move(board, new_pos, blue_pos, history))

        # right
        new_pos = (red_pos[0] + move_dist, red_pos[1])
        if new_pos[0] < len(board) and new_pos != blue_pos:
            move_results.append(calc_move(board, new_pos, blue_pos, history))

    # ===================
    # check blue positions
    # ===================

    if blue_pos != (0, 0):  # if blue has made it, no need to move it anymore

        move_dist = board[blue_pos[0]][blue_pos[1]]

        # up
        new_pos = (blue_pos[0], blue_pos[1] - move_dist)
        if new_pos[1] >= 0 and new_pos != blue_pos:
            move_results.append(calc_move(board, red_pos, new_pos, history))

        # down
        new_pos = (blue_pos[0], blue_pos[1] + move_dist)
        if new_pos[1] < len(board) and new_pos != blue_pos:
            move_results.append(calc_move(board, red_pos, new_pos, history))

        # left
        new_pos = (blue_pos[0] - move_dist, blue_pos[1])
        if new_pos[0] >= 0 and new_pos != blue_pos:
            move_results.append(calc_move(board, red_pos, new_pos, history))

        # right
        new_pos = (blue_pos[0] + move_dist, blue_pos[1])
        if new_pos[0] < len(board) and new_pos != blue_pos:
            move_results.append(calc_move(board, red_pos, new_pos, history))

    best_move_count = min(move_results)
    return best_move_count


def calc_move(board, red_pos, blue_pos, history):
    """
    Returns the the cached result for the passed state, or calls
    calculate_best_move if the cache misses.
    """

    if (red_pos, blue_pos) in history:
        print(f"Hit cache: f{(red_pos, blue_pos)}")
        return history[(red_pos, blue_pos)]
    else:
        r = calculate_best_move(board, red_pos, blue_pos, history)
        history[(red_pos, blue_pos)] = r
        return r
