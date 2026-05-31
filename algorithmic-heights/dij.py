# Dijkstra's Algorithm (DIJ)
# Rosalind problem: https://rosalind.info/problems/dij/
#
# Problem: Given a weighted directed graph with non-negative edge weights,
# find the shortest distances from node 1 to all other nodes.
# Output -1 for unreachable nodes.
#
# Algorithm: Dijkstra's with a min-heap priority queue. O((n+m) log n).

import os
import sys
import heapq
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_dij.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    for line in lines[1:m+1]:
        u, v, w = map(int, line.split())
        adj[u].append((v, w))

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    print(' '.join(str(dist[i]) if dist[i] != INF else '-1' for i in range(1, n+1)))

if __name__ == '__main__':
    solve(get_input())
