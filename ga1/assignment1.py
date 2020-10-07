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

    # Dict of delegates arranged by parties
    parties = {0: [0]}

    for curr_person in range(1,n):
        print(f"Checking person {curr_person}")
        in_known_party = False
        for party in parties:
            print(f"  against party {party}")
            if same_party(curr_person, parties[party][0]):
                parties[party].append(curr_person)
                in_known_party = True
                break

        if not in_known_party:
            parties[len(parties)] = [curr_person]

    print(f"\nParties dict:")
    print(parties)
