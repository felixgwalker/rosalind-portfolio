# Bellman-Ford Algorithm (BF)
# Rosalind problem: https://rosalind.info/problems/bf/
#
# Problem: Given a weighted directed graph (possibly with negative edges but
# guaranteed no negative cycles), compute shortest path distances from node 1.
# Output -1 for unreachable nodes.
# Algorithm: Bellman-Ford — relax all edges n-1 times. O(n·m).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_bf.txt')
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

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    print(' '.join(str(dist[i]) if dist[i] != INF else '-1' for i in range(1, n+1)))

if __name__ == '__main__':
    solve(get_input())
