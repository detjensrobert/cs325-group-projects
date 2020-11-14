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

    moves = 0

    red_pos = (0, 0)
    blue_pos = (board_size - 1, board_size - 1)

    board = infile.readlines()
    # split lines into each space & convert to ints
    board = [list(map(int, line.strip().split(","))) for line in board]

    print(f"Board size: {board_size}x{board_size}")
    print(numpy.matrix(board))

    outfile.write(str(moves))
    infile.close()
    outfile.close()
    return moves
