# Strongly Connected Components (SCC)
# Rosalind problem: https://rosalind.info/problems/scc/
#
# Problem: Given a directed graph, find the number of strongly connected components.
# Algorithm: Kosaraju's two-pass DFS — first pass records finish order on the
# original graph; second pass processes the reversed graph in reverse finish order,
# each DFS tree forming one SCC. O(n + m).

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_scc.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    radj = defaultdict(list)
    for line in lines[1:m+1]:
        u, v = map(int, line.split())
        adj[u].append(v)
        radj[v].append(u)

    # First pass: iterative DFS recording finish order
    visited = [False] * (n + 1)
    order = []

    def dfs1(start):
        stack = [(start, False)]
        while stack:
            u, done = stack.pop()
            if done:
                order.append(u)
                continue
            if visited[u]:
                continue
            visited[u] = True
            stack.append((u, True))
            for v in adj[u]:
                if not visited[v]:
                    stack.append((v, False))

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    # Second pass: DFS on reversed graph in decreasing finish time
    visited2 = [False] * (n + 1)
    scc_count = 0

    def dfs2(start):
        stack = [start]
        while stack:
            u = stack.pop()
            if visited2[u]:
                continue
            visited2[u] = True
            for v in radj[u]:
                if not visited2[v]:
                    stack.append(v)

    for u in reversed(order):
        if not visited2[u]:
            dfs2(u)
            scc_count += 1

    print(scc_count)

if __name__ == '__main__':
    solve(get_input())
