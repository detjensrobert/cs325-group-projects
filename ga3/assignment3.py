"""
    This file contains the template for Assignment3.  For testing it, I will
    place it in a different directory, call the function <vidrach_itky_leda>,
    and check its output. So, you can add/remove  whatever you want to/from
    this file.  But, don't change the name of the file or the name/signature
    of the following function.

    Also, I will use <python3> to run this code.
"""

import numpy  # for better matrix printing
import sys

debug = False


def vidrach_itky_leda(input_file_path, output_file_path):
    """
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    """

    infile = open(input_file_path, mode="r")

    board_size = int(infile.readline())

    board = infile.readlines()
    # split lines into each space & convert to ints
    board = [list(map(int, line.strip().split(","))) for line in board]

    infile.close()

    red_pos = (0, 0)
    blue_pos = (board_size - 1, board_size - 1)

    if debug:
        print(f"Board size: {board_size}x{board_size}")
        print(numpy.matrix(board))

    moves = gen_all_moves(board, red_pos, blue_pos, []) - 1

    outfile = open(output_file_path, mode="w")
    outfile.write(str(moves))
    outfile.close()
    return moves


def gen_all_moves(board, red_pos, blue_pos, previous_moves, indent=0):
    """
    Walks through all possible moves from the current position.
    """

    indent = indent + 4

    board_size = len(board)

    current_moves = previous_moves + [(red_pos, blue_pos)]

    if debug:
        print(" " * indent + f"Checking r{red_pos} b{blue_pos}")
        a = [["-" for _ in row] for row in board]
        a[red_pos[0]][red_pos[1]] = "R"
        a[blue_pos[0]][blue_pos[1]] = "B"
        # print(numpy.matrix(a))
        print(" " * indent + f"Current move history: {current_moves}")

    # if we are at the end state, return the current moveset that got us here
    if red_pos == (board_size - 1, board_size - 1) and blue_pos == (0, 0):
        if debug:
            print(" " * indent + "Reached the end!")
        return len(current_moves)

    # if we have been here before, return the memoised state.

    # otherwise, explore all moves we can do from here
    # if we run into a state we have already been to,
    # stop as its already been searched.

    move_results = []

    # check all red moves
    if red_pos != (board_size - 1, board_size - 1):
        move_dist = board[blue_pos[0]][blue_pos[1]]

        # up
        new_pos = (red_pos[0], red_pos[1] - move_dist)
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[1] >= 0
            and new_pos != blue_pos
            and (new_pos, blue_pos) not in previous_moves
        ):
            r = gen_all_moves(board, new_pos, blue_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

        # down
        new_pos = (red_pos[0], red_pos[1] + move_dist)
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[1] < len(board)
            and new_pos != blue_pos
            and (new_pos, blue_pos) not in previous_moves
        ):
            r = gen_all_moves(board, new_pos, blue_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

        # left
        new_pos = (red_pos[0] - move_dist, red_pos[1])
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[0] >= 0
            and new_pos != blue_pos
            and (new_pos, blue_pos) not in previous_moves
        ):
            r = gen_all_moves(board, new_pos, blue_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

        # right
        new_pos = (red_pos[0] + move_dist, red_pos[1])
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[0] < len(board)
            and new_pos != blue_pos
            and (new_pos, blue_pos) not in previous_moves
        ):
            r = gen_all_moves(board, new_pos, blue_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

    # check all blue moves
    if blue_pos != (0, 0):
        move_dist = board[red_pos[0]][red_pos[1]]

        # up
        new_pos = (blue_pos[0], blue_pos[1] - move_dist)
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[1] >= 0
            and new_pos != red_pos
            and (red_pos, new_pos) not in previous_moves
        ):
            r = gen_all_moves(board, red_pos, new_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

        # down
        new_pos = (blue_pos[0], blue_pos[1] + move_dist)
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[1] < len(board)
            and new_pos != red_pos
            and (red_pos, new_pos) not in previous_moves
        ):
            r = gen_all_moves(board, red_pos, new_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

        # left
        new_pos = (blue_pos[0] - move_dist, blue_pos[1])
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[0] >= 0
            and new_pos != red_pos
            and (red_pos, new_pos) not in previous_moves
        ):
            r = gen_all_moves(board, red_pos, new_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

        # right
        new_pos = (blue_pos[0] + move_dist, blue_pos[1])
        if (  # if in-bounds, not occupied, and has not been visited before
            new_pos[0] < len(board)
            and new_pos != red_pos
            and (red_pos, new_pos) not in previous_moves
        ):
            r = gen_all_moves(board, red_pos, new_pos, current_moves, indent)
            if debug:
                print(" " * indent + f"returned: {r}")
            move_results.append(r)

    # find best path out of the ones given
    return min(move_results, default=sys.maxsize)

    """
    tree
    of all moves
    remove leafs that do not end

    return true if at end state
    return false if we've been everywhere
    recursively call
    """
