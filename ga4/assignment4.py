# This file contains the template for Assignment4. For testing it, I will
# place it in a different directory, call the function <first_second_third_mst>
# and check its output. So, you can add/remove whatever you want to/from this
# file.  But, don't change the name of the file or the name/signature of the
# following function.
#
# Also, I will use <python3> to run this code.


def first_second_third_mst(input_file_path, output_file_path):
    """
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    """

    infile = open(input_file_path, mode="r")

    graph_size = int(infile.readline())

    # split lines into each space & convert to ints
    graph = [list(map(int, line.strip().split(","))) for line in infile.readlines()]

    infile.close()

    # import numpy
    # print(f"Board size: {board_size}x{board_size}")
    # print(numpy.matrix(board))

    tree_weights = (calc_first(graph), calc_second(graph), calc_third(graph))

    outfile = open(output_file_path, mode="w")
    outfile.write(" ".join(map(str, tree_weights)))
    outfile.close()
    return tree_weights


def calc_first(graph):
    pass


def calc_second(graph):
    pass


def calc_third(graph):
    pass
