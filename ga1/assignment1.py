"""
    This file contains the template for Assignment1.  You should fill the
    function <majority_party_size>.  The function, recieves two inputs:
      (1) n: the number of delegates in the room, and
      (2) same_party(int, int): a function that can be used to check if two members are
      in the same party.

    Your algorithm in the end should return the size of the largest party, assuming
    it is larger than n/2.

    I will use <python3> to run this code.
"""


def majority_party_size(n, same_party):
    """
    n (int): number of people in the room.
    same_party (func(int, int)): This function determines if two delegates
        belong to the same party.  same_party(i,j) is True if i, j belong to
        the same party (in particular, if i = j), False, otherwise.

    return: The number of delegates in the majority party.  You can assume
        more than half of the delegates belong to the same party.
    """
    return majority_party_size_helper([i for i in range(n)], same_party)[1]


def majority_party_size_helper(delegates, same_party):
    # PARAM: delegates[] = indexes of delegates to check
    # RETURN: tuple(index of majority party candidate, size of majority party)

    if len(delegates) >= 2:
        # recursively check each half of our delegate list to find the majority party of each half
        mid = int(len(delegates) / 2)
        (left_delegate, _) = majority_party_size_helper(delegates[:mid], same_party)
        (right_delegate, _) = majority_party_size_helper(delegates[mid:], same_party)

        # Count up the size of each half's majority party for the whole chunk
        left_party_size = 0
        right_party_size = 0
        for i in delegates:
            if same_party(left_delegate, i):
                left_party_size += 1
            if same_party(left_delegate, i):
                right_party_size += 1

        # who's bigger?
        if left_party_size > right_party_size:
            maj_delegate = left_delegate
            maj_size = left_party_size
        else:
            maj_delegate = right_delegate
            maj_size = right_party_size

        return (maj_delegate, maj_size)
    else: # Base case: single delegate -- only one possible majority here!
        return (delegates[0], 1)
