"""
    This file contains the template for Assignment3.  For testing it, I will
    place it in a different directory, call the function <vidrach_itky_leda>,
    and check its output. So, you can add/remove  whatever you want to/from
    this file.  But, don't change the name of the file or the name/signature
    of the following function.

    Also, I will use <python3> to run this code.
"""

import queue


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

    # import numpy
    # print(f"Board size: {board_size}x{board_size}")
    # print(numpy.matrix(board))

    moves = vidrach_actual(board)

    outfile = open(output_file_path, mode="w")
    outfile.write(str(moves))
    outfile.close()
    return moves


def vidrach_actual(board):
    """
    Walks the board using a breadth-first alg and a queue.
    """
    board_size = len(board)

    # coordinates queue - list of (red_pos, blue_pos) tuples
    posqueue = queue.SimpleQueue()
    posqueue.put(((0, 0), (board_size - 1, board_size - 1)))

    moves = {((0, 0), (board_size - 1, board_size - 1)): 0}

    while not posqueue.empty():
        curr_pos = posqueue.get()
        curr_move = moves[curr_pos]

        red_pos = curr_pos[0]
        blue_pos = curr_pos[1]

        # if at the swapped position, break/return as this is the fastest
        if red_pos == (board_size - 1, board_size - 1) and blue_pos == (0, 0):
            return curr_move

        # check all red moves
        if red_pos != (board_size - 1, board_size - 1):
            move_dist = board[blue_pos[0]][blue_pos[1]]

            # up
            new_pos = (red_pos[0], red_pos[1] - move_dist)
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[1] >= 0
                and new_pos != blue_pos
                and (new_pos, blue_pos) not in moves
            ):
                posqueue.put((new_pos, blue_pos))
                moves[(new_pos, blue_pos)] = curr_move + 1

            # down
            new_pos = (red_pos[0], red_pos[1] + move_dist)
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[1] < board_size
                and new_pos != blue_pos
                and (new_pos, blue_pos) not in moves
            ):
                posqueue.put((new_pos, blue_pos))
                moves[(new_pos, blue_pos)] = curr_move + 1

            # left
            new_pos = (red_pos[0] - move_dist, red_pos[1])
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[0] >= 0
                and new_pos != blue_pos
                and (new_pos, blue_pos) not in moves
            ):
                posqueue.put((new_pos, blue_pos))
                moves[(new_pos, blue_pos)] = curr_move + 1

            # right
            new_pos = (red_pos[0] + move_dist, red_pos[1])
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[0] < board_size
                and new_pos != blue_pos
                and (new_pos, blue_pos) not in moves
            ):
                posqueue.put((new_pos, blue_pos))
                moves[(new_pos, blue_pos)] = curr_move + 1

        # check all blue moves
        if blue_pos != (0, 0):
            move_dist = board[red_pos[0]][red_pos[1]]

            # up
            new_pos = (blue_pos[0], blue_pos[1] - move_dist)
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[1] >= 0
                and new_pos != red_pos
                and (red_pos, new_pos) not in moves
            ):
                posqueue.put((red_pos, new_pos))
                moves[(red_pos, new_pos)] = curr_move + 1

            # down
            new_pos = (blue_pos[0], blue_pos[1] + move_dist)
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[1] < board_size
                and new_pos != red_pos
                and (red_pos, new_pos) not in moves
            ):
                posqueue.put((red_pos, new_pos))
                moves[(red_pos, new_pos)] = curr_move + 1

            # left
            new_pos = (blue_pos[0] - move_dist, blue_pos[1])
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[0] >= 0
                and new_pos != red_pos
                and (red_pos, new_pos) not in moves
            ):
                posqueue.put((red_pos, new_pos))
                moves[(red_pos, new_pos)] = curr_move + 1

            # right
            new_pos = (blue_pos[0] + move_dist, blue_pos[1])
            if (  # if in-bounds, not occupied, and has not been visited before
                new_pos[0] < board_size
                and new_pos != red_pos
                and (red_pos, new_pos) not in moves
            ):
                posqueue.put((red_pos, new_pos))
                moves[(red_pos, new_pos)] = curr_move + 1
