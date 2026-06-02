# BA4M — Solve the Turnpike Problem
# https://rosalind.info/problems/ba4m/
#
# Given: A collection of integers L.
# Return: A set A of integers such that ΔA = L (the multiset of all pairwise
#         absolute differences between elements of A equals L).

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba4m.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def can_place(x, points, D):
    for p in points:
        d = abs(x - p)
        if D[d] <= 0:
            return False
        D[d] -= 1
    return True

def undo_place(x, points, D):
    for p in points:
        d = abs(x - p)
        D[d] += 1

def backtrack(D, points, x_max):
    remaining = [d for d, c in D.items() if c > 0]
    if not remaining:
        return list(points)
    y = max(remaining)
    # Try placing at y
    if can_place(y, points, D):
        points.add(y)
        result = backtrack(D, points, x_max)
        if result is not None:
            return result
        points.remove(y)
        undo_place(y, points, D)
    # Try placing at x_max - y
    z = x_max - y
    if z != y:
        if can_place(z, points, D):
            points.add(z)
            result = backtrack(D, points, x_max)
            if result is not None:
                return result
            points.remove(z)
            undo_place(z, points, D)
    return None

def solve(data):
    L = list(map(int, data.split()))
    D = Counter(L)
    x_max = max(L)
    points = {0, x_max}
    D[x_max] -= 1
    # Remove 0 from D if it appears (distances of 0 exist only if duplicate points)
    result = backtrack(D, points, x_max)
    if result:
        print(' '.join(map(str, sorted(result))))

if __name__ == '__main__': solve(get_input())
