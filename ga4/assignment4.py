# This file contains the template for Assignment4. For testing it, I will
# place it in a different directory, call the function <first_second_third_mst>
# and check its output. So, you can add/remove whatever you want to/from this
# file.  But, don't change the name of the file or the name/signature of the
# following function.
#
# Also, I will use <python3> to run this code.

import queue
import sys
import numpy

debug = True


def p(msg):
    if debug:
        print(msg)


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

    tree_weights = (
        calc_first(graph, graph_size),
        calc_second(graph, graph_size),
        calc_third(graph, graph_size),
    )

    outfile = open(output_file_path, mode="w")
    outfile.write("\n".join(map(str, tree_weights)))
    outfile.close()
    return tree_weights


def calc_mst(graph, graph_size):
    nodequeue = queue.PriorityQueue()
    weights = []
    visited = {}

    p("Current graph:")
    p(numpy.matrix(graph))

    # add initial node
    # queue format: (weight, from_node, to_node)
    nodequeue.put((0, 0, 0))

    while not nodequeue.empty():
        queue_elem = nodequeue.get()
        weight = queue_elem[0]
        parent = queue_elem[1]
        node = queue_elem[2]

        if node not in visited:
            p(f"on: {parent}->{node} ({weight})")
            visited[node] = True
            weights.append((parent, node))

            for dest_node, dest_weight in enumerate(graph[node]):
                if dest_weight == -1:  # -1 disables the connection, so ignore it
                    continue
                nodequeue.put((dest_weight, node, dest_node))

    return weights


def calc_first(graph, graph_size):
    p("=== FIRST ===")

    weights = calc_mst(graph, graph_size)

    return sum(list(map(lambda w: graph[w[0]][w[1]], weights)))


def calc_second(graph, graph_size):
    p("=== SECOND ===")

    weights = calc_mst(graph, graph_size)

    # find largest connection, disable it to find next best MST
    big = max(weights, key=lambda w: graph[w[0]][w[1]])
    p(f"worst connection: {big[0]}->{big[1]} ({graph[big[0]][big[1]]})")

    graph[big[0]][big[1]] = -1

    weights = calc_mst(graph, graph_size)

    return sum(list(map(lambda w: graph[w[0]][w[1]], weights)))


def calc_third(graph, graph_size):
    p("=== THIRD ===")

    weights = calc_mst(graph, graph_size)

    # find largest connection, disable it to find next best MST
    big = max(weights, key=lambda w: graph[w[0]][w[1]])
    p(f"worst connection: {big[0]}->{big[1]} ({graph[big[0]][big[1]]})")

    graph[big[0]][big[1]] = -1

    weights = calc_mst(graph, graph_size)

    # find largest connection, disable it to find next best MST
    big = max(weights, key=lambda w: graph[w[0]][w[1]])
    p(f"worst connection: {big[0]}->{big[1]} ({graph[big[0]][big[1]]})")

    graph[big[0]][big[1]] =  -1

    weights = calc_mst(graph, graph_size)

    return sum(list(map(lambda w: graph[w[0]][w[1]], weights)))
