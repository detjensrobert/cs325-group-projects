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


# def majority_party_size(n, same_party):
#     """
#     n (int): number of people in the room.
#     same_party (func(int, int)): This function determines if two delegates
#         belong to the same party.  same_party(i,j) is True if i, j belong to
#         the same party (in particular, if i = j), False, otherwise.

#     return: The number of delegates in the majority party.  You can assume
#         more than half of the delegates belong to the same party.
#     """

#     # Dict of delegates arranged by parties
#     parties = {0: [0]}

#     for curr_person in range(1, n):
#         in_known_party = False

#         for party in parties:
#             # is this person in a known party?
#             if same_party(curr_person, parties[party][0]):
#                 # if so, add them to that party
#                 parties[party].append(curr_person)
#                 in_known_party = True

#                 # check if this is now the largest party
#                 # and move it to the front if so
#                 if party != 0 and len(parties[party]) > len(parties[0]):
#                     move_to_front(parties, party)

#                 break

#         # if not, add them to a new party
#         if not in_known_party:
#             parties[len(parties)] = [curr_person]

#     return len(parties[0])


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
        m = []
        for i in range(n):
            m.append(i)
        n = m

    if len(n) > 0:
        m = round(len(n)/2)
        left = majority_party_size(n[:m], same_party)
        right = majority_party_size(n[m+1:], same_party)

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

def move_to_front(hash, id):
    temp = hash[id]
    for i in range(id, 0, -1):
        hash[i] = hash[i-1]
    hash[0] = temp


"""
recurse down until subarrays of <=2 elems
compare first pair with next layer up
  pair: cand[0] and cand[1]
  see which cand has majority in the previous level
"""
