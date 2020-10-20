def vankin_max_score(input_file_path, output_file_path):

    infile = open(input_file_path, mode='r')
    outfile = open(output_file_path, mode='w')

    max_score = None

    board_size = int(infile.readline())

    board = infile.readlines()
    board = [line.strip().split(' ') for line in board]  # split lines into squares
    board = [list(map(lambda x: int(x), line)) for line in board]  # convert squares to ints

    print(f"Board size: {board_size}x{board_size}")
    print(board)

    outfile.write(str(max_score))
    infile.close()
    outfile.close()
    return max_score
