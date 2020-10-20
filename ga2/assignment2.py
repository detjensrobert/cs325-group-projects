import numpy  # for matrix printing


def vankin_max_score(input_file_path, output_file_path):

    infile = open(input_file_path, mode="r")
    outfile = open(output_file_path, mode="w")

    max_score = 0

    board_size = int(infile.readline())

    board = infile.readlines()
    # split lines into squares & convert to ints
    board = [list(map(int, line.strip().split(","))) for line in board]
    scores = [[0 for _ in range(board_size)] for _ in range(board_size)]

    print(f"Board size: {board_size}x{board_size}")
    print(numpy.matrix(board))

    # iterate over board matrix backwards (with index)
    for i, row in reversed(list(enumerate(board))):
        for j, val in reversed(list(enumerate(row))):
            scores[i][j] = get_max_score(board, scores, board_size, i, j)

            max_score = max(scores[i][j], max_score)

    print("Scores:")
    print(numpy.matrix(scores))

    outfile.write(str(max_score))
    infile.close()
    outfile.close()
    return max_score


# returns the max score of either the lower or adjacent value
def get_max_score(board, scores, board_size, row, col):
    lower_score = board[row][col]
    right_score = board[row][col]

    # check score if move down
    if row + 1 < board_size:  # not out of bounds
        lower_score += scores[row + 1][col]

    # check score if move right
    if col + 1 < board_size:  # not out of bounds
        right_score += scores[row][col + 1]

    return max(lower_score, right_score)
