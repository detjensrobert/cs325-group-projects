# This file contains the template for Assignment4. For testing it, I will
# place it in a different directory, call the function <first_second_third_mst>
# and check its output. So, you can add/remove whatever you want to/from this
# file.  But, don't change the name of the file or the name/signature of the
# following function.
#
# Also, I will use <python3> to run this code.

import queue


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

    first_mst = calc_mst(graph, graph_size)["connections"]

    # try removing each connection in the MST and recalculating the total weight
    weights = []
    for p, c in first_mst:
        old_val = graph[p][c]
        graph[p][c] = -1
        weights.append(calc_mst(graph, graph_size)["total_weight"])
        graph[p][c] = old_val

    weights.sort()
    first = weights[0] + 1
    second = weights[1]
    third = weights[2]

    outfile = open(output_file_path, mode="w")
    outfile.write(f"{first}\n{second}\n{third}\n")
    outfile.close()
    return (first, second, third)


def calc_mst(graph, graph_size):
    nodequeue = queue.PriorityQueue()
    connections = []
    visited = {}

    # add initial node
    # queue format: (weight, from_node, to_node)
    nodequeue.put((0, 0, 0))
    weight = 0

    while not nodequeue.empty():
        queue_elem = nodequeue.get()
        parent = queue_elem[1]
        node = queue_elem[2]

        if node not in visited:
            visited[node] = True
            connections.append((parent, node))
            weight += graph[parent][node]

            for dest_node, dest_weight in enumerate(graph[node]):
                if dest_weight != -1:  # -1 disables the connection, so ignore it
                    nodequeue.put((dest_weight, node, dest_node))

    return {"connections": connections, "total_weight": weight}
