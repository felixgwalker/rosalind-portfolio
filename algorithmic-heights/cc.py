# Connected Components (CC)
# Rosalind problem: https://rosalind.info/problems/cc/
#
# Problem: Given an undirected graph, count the number of connected components.
#
# Algorithm: Union-Find or BFS/DFS from each unvisited node. O(n + m).

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_cc.txt')
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

    visited = set()
    components = 0

    for start in range(1, n + 1):
        if start not in visited:
            components += 1
            # BFS to mark all nodes in this component
            queue = deque([start])
            visited.add(start)
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)

    print(components)

if __name__ == '__main__':
    solve(get_input())
