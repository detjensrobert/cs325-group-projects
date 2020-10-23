# CS 325 Group Project 2

## Robert Detjens, Srikar Valluri, Felix Brucker

---

### Scenario

Vankin’s Mile is an American solitaire game played on an $n$ × $n$ square grid. The player starts by placing a token on any square of the grid. Then on each turn, the player moves the token either one square to the right or one square down. The game ends when player moves the token off the edge of the board. Each square of the grid has a numerical value, which could be positive, negative, or zero. The player starts with a score of zero; whenever the token lands on a square, the player
adds its value to his score. The object of the game is to score as many points as possible.

In this assignment, you describe and analyze an efficient algorithm to compute the maximum possible score for a game of Vankin’s Mile, given the $n$ × $n$ array of values as input.

### Description

Our algorithm uses a memoization apprach, that saves multiple computations, especially at the end of the algorithm where the steps become relatively large. We achieve this in $O(n) = n^2$

We have implemented two functions to solve this problem. 

The function get_max_score determines the score of traversing in either the right or down directions by one square, and returns the maximum of those two values. Since we don't actually care about the path taken by the player in this implementation, but rather just their score, we only need to keep track of the maximum score for that particular location.

The function vankin_max_score uses the get_max_score function to actually traverse the board, and determine the best possible score per location. To store every score at every position in the array, it uses a seperate array called scores. By starting from the bottom right of the board, it starts by filling the scores matrix with the values while traversing to the bottom left. This is possible due to the fact that we know every value to the right (as it was already computed) as we traverse left. We also know this is possible because there are no values at the bottom yet, so there's only one direction of movement. Once we determine the values of the bottom row, we start at the row that's higher by one, and once again start from right to left. Using the process of memoization, we only have to refer to two values per iteration when we traverse the entire matrix, as we are computing the best possible values for that particular location. 

### Runtime Analysis

Since we have to traverse every location in the entire $n$ x $n$ array, and since there are %n^2% amount of squares, we determine that this is going to be $O(n) = n^2$.
