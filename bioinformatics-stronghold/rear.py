# Reversal Distance (REAR)
# Rosalind problem: https://rosalind.info/problems/rear/
#
# Problem: Given 5 pairs of permutations (each of {1,...,n}, n ≤ 10), compute
# the reversal distance for each pair — the minimum number of reversals
# (of contiguous sub-sequences) needed to transform the first into the second.
#
# Algorithm: BFS from the source permutation, treating each reachable permutation
# as a state. The BFS layer at which we first reach the target gives the distance.
# This is feasible for n ≤ 10 (10! = 3.6M states, but BFS explores far fewer
# in practice because most instances need only a small number of reversals).

import os
import sys
from collections import deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_rear.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def reversal_distance(src, tgt):
    """BFS to find minimum reversals transforming tuple src into tuple tgt."""
    if src == tgt:
        return 0
    n = len(src)
    visited = {src: 0}
    queue = deque([src])
    while queue:
        perm = queue.popleft()
        dist = visited[perm]
        # Try all possible reversals of sub-sequences [i..j]
        perm_list = list(perm)
        for i in range(n):
            for j in range(i + 1, n):
                new_perm = tuple(perm_list[:i] + perm_list[i:j+1][::-1] + perm_list[j+1:])
                if new_perm == tgt:
                    return dist + 1
                if new_perm not in visited:
                    visited[new_perm] = dist + 1
                    queue.append(new_perm)
    return -1   # should never reach here for valid input

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    results = []
    i = 0
    while i < len(lines):
        src = tuple(map(int, lines[i].split()))
        tgt = tuple(map(int, lines[i+1].split()))
        results.append(reversal_distance(src, tgt))
        i += 2
    print(' '.join(map(str, results)))

if __name__ == '__main__':
    solve(get_input())
