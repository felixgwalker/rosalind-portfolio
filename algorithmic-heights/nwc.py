# Negative Weight Cycle (NWC)
# Rosalind problem: https://rosalind.info/problems/nwc/
#
# Problem: Given a weighted directed graph, determine if it contains a negative
# weight cycle. Output -1 if a negative cycle exists, 1 otherwise.
# Algorithm: Bellman-Ford initialised to 0 (detects any reachable negative cycle,
# not just from node 1). A further relaxation on the n-th pass signals a cycle.
# O(n·m).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_nwc.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    edges = []
    for line in lines[1:m+1]:
        u, v, w = map(int, line.split())
        edges.append((u, v, w))

    # Initialise all distances to 0 so we detect any negative cycle in the graph
    dist = [0] * (n + 1)

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print(-1)
            return
    print(1)

if __name__ == '__main__':
    solve(get_input())
