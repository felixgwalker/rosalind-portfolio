# Double-Degree Array (DDEG)
# Rosalind problem: https://rosalind.info/problems/ddeg/
#
# Problem: Given an undirected graph, compute the double-degree of each node:
# the sum of the degrees of all its neighbours.
# Output: n integers, one per node (in order 1..n).
#
# Algorithm: Build an adjacency list, compute degree of each node, then for
# each node sum the degrees of its neighbours. O(n + m).

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_ddeg.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    for line in lines[1:m+1]:
        u, v = map(int, line.split())
        adj[u].append(v)
        adj[v].append(u)
    degree = {i: len(adj[i]) for i in range(1, n+1)}
    double_deg = [sum(degree[nb] for nb in adj[v]) for v in range(1, n+1)]
    print(' '.join(map(str, double_deg)))

if __name__ == '__main__':
    solve(get_input())
