# CS 325 Group Project 4

## Robert Detjens, Srikar Valluri, Felix Brucker

---

### Scenario

In class, we have seen multiple algorithms for computing minimum spanning trees. In this assignment, we design algorithms for computing the second and third minimum spanning trees. For example, the following figure shows a graph, and its first, second, and third minimum spanning trees.

![Example of first, second, and third MSTs](https://i.imgur.com/qefuIRg.png)

### Algorithm Description

The base algorithm used is Prim’s algorithm. An arbitrary node is the starting point. Starting with it, nodes are added to a singular forest of vertices. Each step of the algorithm, all the edges connected to but not in the forest are evaluated. The one with the smallest weight is chosen and the node it leads to is added to the forest. This continues until all nodes in the graph are part of the forest. To find the first minimum spanning tree, it is implemented in the following way. A priority queue stores nearby edges as the graph is traversed. The lightest edges are retrieved first and marked as visited. This continues until the queue is exhausted.
The program in its entirety calculates the first MST simply using Prim’s algorithm. Another approach finds the second and third MSTs. A series of graphs are ran through Prim’s algorithm, each missing a unique edge that was included in the first MST. There is one graph for each possible missing edge. The resulting MSTs are ranked by total weight and the two lightest are the second and third MSTs respectively.

### Runtime Analysis

When run on the graph and memoized with the queue, Prim’s algorithm has a known runtime of O( E log V ), where E is the number of edges and V is the amount of vertices in the graph. The program is deployed once for every edge in the first minimum spanning tree, plus one time to get the first MST. The amount of repetition is approximately E, so the big O of the entire program is O( E^2 log V ).

### Proof of Correctness

Prim’s algorithm is known to correctly find the first minimum spanning tree. The second and third MSTs are correct by the following reasoning. 
Every edge in the first MST is tested against any possible replacements. Out of all combinations possible of edges and their replacements, the one with the least difference between edge and replacement is chosen for the second MST. The one with the second least difference is the third MST. These MSTs must be correct because all possibilities were exhaustively searched and ranked.
