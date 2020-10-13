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

    if len(delegates) > 2:
        # recursively check each half of our candidate list (n[1]) to find the majority of each half
        mid = int(len(delegates) / 2)
        left = majority_party_size_helper(delegates[:mid], same_party)
        right = majority_party_size_helper(delegates[mid:], same_party)

        # See which side's majority is the majority for our whole chunk
        left_same = 0
        right_same = 0
        for i in delegates:
            if same_party(left[0], i):
                left_same += 1
            if same_party(right[0], i):
                right_same += 1

        if left_same > right_same:
            x = left[0]
        else:
            x = right[0]

        return (x, max(left_same, right_same))
    else:
        return (delegates[0], 1)
