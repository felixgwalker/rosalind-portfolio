# Testing Bipartiteness (BIP)
# Rosalind problem: https://rosalind.info/problems/bip/
#
# Problem: Given an undirected graph, determine if it is bipartite (2-colorable).
# A graph is bipartite iff it contains no odd-length cycle.
# Algorithm: BFS 2-coloring across all connected components. O(n + m).

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_bip.txt')
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

    color = [-1] * (n + 1)
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    print(-1)
                    return
    print(1)

if __name__ == '__main__':
    solve(get_input())
