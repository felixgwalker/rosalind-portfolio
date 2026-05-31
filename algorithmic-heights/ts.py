# Topological Sorting (TS)
# Rosalind problem: https://rosalind.info/problems/ts/
#
# Problem: Given a directed acyclic graph, output a valid topological ordering
# of its nodes. (Multiple valid orderings exist; any one is accepted.)
#
# Algorithm: Kahn's algorithm — repeatedly remove nodes with in-degree 0. O(n+m).

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_ts.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    in_degree = defaultdict(int)
    for node in range(1, n + 1):
        in_degree[node] = in_degree.get(node, 0)   # initialise
    for line in lines[1:m+1]:
        u, v = map(int, line.split())
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque(node for node in range(1, n+1) if in_degree[node] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    print(' '.join(map(str, order)))

if __name__ == '__main__':
    solve(get_input())
