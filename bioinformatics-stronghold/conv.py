# Comparing Spectra with the Spectral Convolution (CONV)
# Rosalind problem: https://rosalind.info/problems/conv/
#
# Problem: Given two multisets S and T of positive real numbers (mass spectra),
# compute the Minkowski difference (spectral convolution): the multiset of all
# differences s-t for s in S, t in T. Return the most common difference
# (the "shift") and its multiplicity.
#
# The spectral convolution peak identifies how much one spectrum needs to be
# shifted to best align with the other.
#
# Algorithm: Compute all pairwise differences, count with a dictionary,
# find the maximum count. O(|S|·|T|).

import os
import sys
from collections import Counter

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_conv.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    S = list(map(float, lines[0].split()))
    T = list(map(float, lines[1].split()))

    # Compute all pairwise differences; round to avoid floating-point issues
    diffs = Counter()
    for s in S:
        for t in T:
            d = round(s - t, 5)
            diffs[d] += 1

    # Find the difference with the highest multiplicity
    best_diff = max(diffs, key=diffs.get)
    print(diffs[best_diff])
    print(best_diff)

if __name__ == '__main__':
    solve(get_input())
