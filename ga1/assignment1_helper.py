#!/usr/bin/env python3
import math
import random

import assignment1

### Helper functions for Group Assignment 1

def same_party(x, y):
    global number_of_queries
    number_of_queries += 1

    if x < 0 or y < 0 or x >= number_of_delegates or y >= number_of_delegates:
        return None
    return delegate_parties[x] == delegate_parties[y]


## MEGA SUPER ULTRA TEST CASE GENERATOR 9000
# tests your algorithm against 10 arrays on increasing size
for i in range(10, 100, 10):

    # generate a list of half random values, half 1's
    # (this follows the one-party-majority constraint)
    test_arr = [random.randint(1, 10) for _ in range(i)]
    test_arr.extend([1 for _ in range(i)])
    random.shuffle(test_arr)

    # set up the global variables
    delegate_parties = [int(x) for x in test_arr]
    number_of_delegates = len(delegate_parties)
    number_of_queries = 0

    majority_size = assignment1.majority_party_size(number_of_delegates, same_party)

    print(f"""
Testing against {test_arr}:
    Size of the majority:  {majority_size} of {number_of_delegates} ({round(majority_size/number_of_delegates * 100)}%)
    Number of compares:    {number_of_queries}
    Ideal num (n log(n)):  {number_of_delegates * math.log(number_of_delegates)}
    """)
