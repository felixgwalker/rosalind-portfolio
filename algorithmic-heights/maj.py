# Majority Element (MAJ)
# Rosalind problem: https://rosalind.info/problems/maj/
#
# Problem: Given k arrays each of length n, for each array find the majority
# element (appearing more than n/2 times), or -1 if none exists.
# Algorithm: Boyer-Moore majority vote, then verify. O(n) per array.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_maj.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def majority(arr):
    candidate, count = arr[0], 0
    for x in arr:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate if arr.count(candidate) > len(arr) // 2 else -1

def solve(data):
    lines = data.splitlines()
    k, n = map(int, lines[0].split())
    results = []
    for i in range(1, k + 1):
        arr = list(map(int, lines[i].split()))
        results.append(majority(arr))
    print(' '.join(map(str, results)))

if __name__ == '__main__':
    solve(get_input())
