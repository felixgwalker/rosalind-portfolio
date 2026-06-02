# Merging Two Sorted Arrays (MER)
# Rosalind problem: https://rosalind.info/problems/mer/
#
# Problem: Given two sorted arrays, merge them into a single sorted array.
# Algorithm: Standard two-pointer merge. O(n + m).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_mer.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n = int(lines[0])
    A = list(map(int, lines[1].split()))
    m = int(lines[2])
    B = list(map(int, lines[3].split()))

    merged = []
    i = j = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            merged.append(A[i]); i += 1
        else:
            merged.append(B[j]); j += 1
    merged.extend(A[i:])
    merged.extend(B[j:])
    print(' '.join(map(str, merged)))

if __name__ == '__main__':
    solve(get_input())
