# General Sink (GS)
# Rosalind problem: https://rosalind.info/problems/gs/
#
# Problem: Given a directed graph, find a "general sink" — a node with in-degree
# n-1 and out-degree 0 (i.e., all other nodes have edges pointing to it and it
# has no outgoing edges). Output the node if found, or -1.
# Multiple test cases may be given.
#
# Algorithm: O(n²) check for each candidate. Use the elimination trick: a
# universal sink can be found in O(n) by elimination.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_gs.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def find_sink(n, adj_matrix):
    """Find universal sink in adjacency matrix in O(n). Returns node (1-based) or -1."""
    candidate = 0   # 0-indexed candidate
    for i in range(1, n):
        # If there's an edge from candidate to i, candidate can't be sink
        if adj_matrix[candidate][i]:
            candidate = i
    # Verify candidate
    for i in range(n):
        if i == candidate:
            continue
        if not adj_matrix[i][candidate] or adj_matrix[candidate][i]:
            return -1
    return candidate + 1   # 1-based

def solve(data):
    lines = data.splitlines()
    i = 0
    results = []
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        n, m = map(int, line.split())
        # Build adjacency matrix
        adj = [[0] * n for _ in range(n)]
        for j in range(m):
            u, v = map(int, lines[i+1+j].split())
            adj[u-1][v-1] = 1
        results.append(str(find_sink(n, adj)))
        i += m + 1
    print(' '.join(results))

if __name__ == '__main__':
    solve(get_input())
