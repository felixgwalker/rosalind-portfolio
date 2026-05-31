# Weighted Median (MED)
# Rosalind problem: https://rosalind.info/problems/med/
#
# Problem: Given a list of values and their positive weights, find the weighted
# median — the smallest value m such that the sum of weights of values ≤ m
# is at least 1/2 the total weight, AND the sum of weights of values ≥ m is
# at least 1/2 the total weight.
#
# Algorithm: Sort by value, accumulate weights, find the crossing point. O(n log n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_med.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n = int(lines[0])
    values = list(map(float, lines[1].split()))
    weights = list(map(float, lines[2].split()))

    # Sort by value
    pairs = sorted(zip(values, weights))
    total = sum(weights)
    half = total / 2

    cumsum = 0
    for val, w in pairs:
        cumsum += w
        if cumsum >= half:
            print(val)
            return

if __name__ == '__main__':
    solve(get_input())
