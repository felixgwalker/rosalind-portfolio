# Creating a Distance Matrix from Restriction Maps (PDPL)
# Rosalind problem: https://rosalind.info/problems/pdpl/
#
# Problem: Given a multiset L containing all C(n,2) pairwise distances
# between n restriction sites on a linear chromosome, reconstruct the
# positions of those sites (with x₁ = 0).
#
# Algorithm: Skiena's backtracking (turnpike reconstruction).
#   1.  x_n = max(L); fix x₁=0 and x_n.
#   2.  Repeatedly take the current maximum d from the remaining multiset.
#       Try placing a new site at position d or at x_n − d.
#   3.  For each candidate p, check that |p − xᵢ| is in the remaining
#       multiset for every already-placed site xᵢ.  If so, commit and recurse.
#   4.  Backtrack if neither placement works.

import os
import sys
from collections import Counter

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_pdpl.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def try_place(L, positions, x_max):
    if not L:
        return sorted(positions)
    d = max(L)

    for candidate in sorted({d, x_max - d}, reverse=True):
        # Compute distances from candidate to all existing positions
        new_dists = Counter(abs(candidate - p) for p in positions)
        if all(L[dist] >= cnt for dist, cnt in new_dists.items()):
            L2 = L.copy()
            for dist, cnt in new_dists.items():
                L2[dist] -= cnt
                if L2[dist] == 0:
                    del L2[dist]
            result = try_place(L2, positions + [candidate], x_max)
            if result is not None:
                return result
    return None

def solve(data):
    nums = list(map(int, data.split()))
    x_max = max(nums)
    L = Counter(nums)

    # Remove the distance 0→x_max (= x_max) once
    L[x_max] -= 1
    if L[x_max] == 0:
        del L[x_max]

    result = try_place(L, [0, x_max], x_max)
    print(*result)

if __name__ == '__main__':
    solve(get_input())
