# 2-Sum Problem (2SUM)
# Rosalind problem: https://rosalind.info/problems/2sum/
#
# Problem: Given k arrays each of n integers, for each array find two distinct
# indices i, j such that A[i] + A[j] = 0. Output the 1-based indices or -1 -1
# if no such pair exists.
#
# Algorithm: Use a hash set — O(n) per array. For each element x, check if -x
# is already in the set. If so, output indices.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_2sum.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def two_sum(arr):
    """Return (i, j) 1-based such that arr[i-1]+arr[j-1]==0, or (-1,-1)."""
    seen = {}   # value -> 1-based index
    for idx, x in enumerate(arr, 1):
        if -x in seen:
            return (seen[-x], idx)
        seen[x] = idx
    return (-1, -1)

def solve(data):
    lines = data.splitlines()
    k, n = map(int, lines[0].split())
    for i in range(1, k + 1):
        arr = list(map(int, lines[i].split()))
        i1, i2 = two_sum(arr)
        print(i1, i2)

if __name__ == '__main__':
    solve(get_input())
