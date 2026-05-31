# Bellman-Ford Shortest Paths (BFSP)
# Rosalind problem: https://rosalind.info/problems/bfsp/
#
# Problem: Given a weighted directed graph (possibly with negative edges),
# compute shortest path distances from node 1. If a negative cycle is reachable,
# output "NEGATIVE CYCLE". Otherwise output distances (or -1 for unreachable).
#
# Algorithm: Bellman-Ford — relax all edges n-1 times. O(n·m).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_bfsp.txt')
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

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0

    # Relax all edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles on n-th relaxation
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            print("NEGATIVE CYCLE")
            return

    print(' '.join(str(dist[i]) if dist[i] != INF else '-1' for i in range(1, n+1)))

if __name__ == '__main__':
    solve(get_input())
