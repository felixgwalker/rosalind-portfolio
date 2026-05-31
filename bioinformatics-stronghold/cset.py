# Fixing an Inconsistent Character Set (CSET)
# Rosalind problem: https://rosalind.info/problems/cset/
#
# Problem: Given a collection of binary strings (a character table) and a rooted
# binary tree, find the minimum number of characters (binary strings) to remove
# so that all remaining characters are compatible with the tree via the
# perfect phylogeny principle.
#
# Two characters are compatible iff the four-gamete test holds: you cannot
# find all four combinations (00, 01, 10, 11) among any two columns.
#
# Algorithm: Build a compatibility graph where nodes are characters and edges
# connect incompatible pairs. Find the minimum vertex cover (NP-hard in general
# but tractable for small inputs by exhaustive or greedy search).
# For the Rosalind constraints (≤ 10 characters) brute-force removal works.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_cset.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def compatible(c1, c2):
    """Two binary characters are compatible iff they don't show all 4 gametes."""
    pairs = set(zip(c1, c2))
    return not (pairs == {'00','01','10','11'} or len(pairs) == 4)

def all_compatible(chars):
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            if not compatible(chars[i], chars[j]):
                return False
    return True

def solve(data):
    chars = [l.strip() for l in data.splitlines() if l.strip()]
    n = len(chars)
    # Try removing k characters, k = 0, 1, 2, ...
    from itertools import combinations
    for k in range(n + 1):
        for removal in combinations(range(n), k):
            remaining = [chars[i] for i in range(n) if i not in removal]
            if all_compatible(remaining):
                print(k)
                return

if __name__ == '__main__':
    solve(get_input())
