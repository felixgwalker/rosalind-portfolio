# Sorting by Reversals (SORT)
# Rosalind problem: https://rosalind.info/problems/sort/
#
# Problem: Given a signed permutation P, use GreedySorting to sort it to the
# identity permutation. Output each intermediate permutation (including any
# created by single-element reversals to fix signs), one per line.
#
# GreedySorting algorithm (from Compeau & Pevzner):
#   For k = 1 to n:
#     1. If P[k-1] != k: find element k (or -k) at position j >= k,
#        reverse the segment P[k-1..j], then output.
#     2. If P[k-1] == -k: reverse just the single element at position k-1
#        (flip its sign), then output.
#
# The algorithm ensures every reversal brings at least one element to its
# correct position, so it terminates in at most O(n²) reversals.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_sort.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def reverse_segment(perm, i, j):
    """Reverse segment perm[i..j] and negate all elements in it."""
    segment = perm[i:j+1]
    perm[i:j+1] = [-x for x in reversed(segment)]

def fmt_perm(perm):
    return ' '.join((f"+{x}" if x > 0 else str(x)) for x in perm)

def greedy_sort(perm):
    steps = []
    n = len(perm)
    for k in range(1, n + 1):   # k is 1-indexed target value
        idx = k - 1              # 0-indexed current position to fill
        if perm[idx] == k:
            continue             # already correct (positive and in place)
        # Find k or -k at position j >= idx
        j = idx
        while j < n and abs(perm[j]) != k:
            j += 1
        if j < n:
            # Reverse segment [idx, j] (brings |k| to position idx)
            reverse_segment(perm, idx, j)
            steps.append(fmt_perm(perm))
        # Now perm[idx] == -k; flip sign
        if perm[idx] == -k:
            perm[idx] = k
            steps.append(fmt_perm(perm))
    return steps

def solve(data):
    perm = list(map(int, data.split()))
    steps = greedy_sort(perm)
    for step in steps:
        print(step)

if __name__ == '__main__':
    solve(get_input())
