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

    if type(n) == int:
        n = [i for i in range(n)]

    if len(n) > 0:
        mid = round(len(n)/2)
        left = majority_party_size(n[:mid], same_party)
        right = majority_party_size(n[mid+1:], same_party)

        left_same = 0
        right_same = 0

        for i in range(len(n)):
            if same_party(left, i):
                left_same += 1
            if same_party(right, i):
                right_same += 1

        return max(left_same, right_same)
    else:
        return 0


"""
recurse down until subarrays of <=2 elems
compare first pair with next layer up
  pair: cand[0] and cand[1]
  see which cand has majority in the previous level
"""
