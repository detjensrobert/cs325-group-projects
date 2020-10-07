# CS 325 Group Project 1

## Robert Detjens, Srikar Valluri, Felix

---

### Scenario

You are a visitor at a political convention with $n$ delegates; each delegate is a member of exactly one political party. It is impossible to tell which political party any delegate belongs to; in particular, you will be summarily ejected from the convention if you ask.

However, you can determine whether any pair of delegates belong to the same party by introducing them to each other. Members of the same political party always greet each other with smiles and friendly handshakes; members of dffierent parties always greet each other with angry stares and insults.

Suppose more than half of the delegates belong to the same political party. Describe an efficient algorithm that finds out the size of the majority party. The efficiency of your algorithms is measured in terms of the number of pairs of delegates that you introduce to each other. We expect that you need about $O(n\log{n})$ handshakes.

### Description

TLDR: We created a dict of the delegates organized by party and found the party with the most members.

We start by creating a dictionary with the first member as party 0. We then take each member and look through the the current dict to see if they are in the same party as any of the previously-seen members. If they are, add them to the list of delegates from that party, update the majority size if this new list is larger than the current largest, and stop searching. If the delegate is not in any of the known parties, they must be from a new party so create a new entry in the hash for them.

In pseudocode:

```
create new dictionary with just the first member alone in a party
for each delegate:
  for each party in dict:
    is this delegate in the same party as one from this party?
      yes:add them to that party
          is this party now larger than the previous record?
          yes:set the new largest size to this one
      no: keep searching
  if not in any of the known parties:
    create new party entry in dict
    add this member to that party
```
