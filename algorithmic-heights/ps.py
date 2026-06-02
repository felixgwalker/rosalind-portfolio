# Partial Sort (PS)
# Rosalind problem: https://rosalind.info/problems/ps/
#
# Problem: Given an array of n integers and k, return the k smallest elements
# in sorted order.
# Algorithm: Min-heap selection (heapq.nsmallest). O(n log k).

import os
import sys
import heapq

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_ps.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    result = heapq.nsmallest(k, arr)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve(get_input())
