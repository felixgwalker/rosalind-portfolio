# Breadth-First Search (BFS)
# Rosalind problem: https://rosalind.info/problems/bfs/
#
# Problem: Given a directed graph, output the BFS shortest-path distances from
# node 1 to all other nodes. Unreachable nodes get distance -1.
#
# Algorithm: Standard BFS from source node 1. O(n + m).

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_bfs.txt')
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

    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    print(' '.join(map(str, dist[1:])))   # nodes 1 to n

if __name__ == '__main__':
    solve(get_input())
