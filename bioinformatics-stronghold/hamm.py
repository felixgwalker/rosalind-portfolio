# Counting Point Mutations (HAMM)
# Rosalind problem: https://rosalind.info/problems/hamm/
#
# Problem: Given two DNA strings s and t of equal length (≤ 1000 nt), return
# the Hamming distance — the number of positions at which the bases differ.
# This is the minimum number of point mutations needed to convert s into t.
#
# Algorithm: Single linear scan comparing corresponding characters. O(n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_hamm.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    s, t = lines[0].strip(), lines[1].strip()
    # sum(1 for ...) counts mismatches without building an intermediate list
    print(sum(1 for a, b in zip(s, t) if a != b))

if __name__ == '__main__':
    solve(get_input())
