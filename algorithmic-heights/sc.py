# Semi-Connected Graph (SC)
# Rosalind problem: https://rosalind.info/problems/sc/
#
# Problem: A directed graph is semi-connected if for every pair of nodes u, v,
# there exists a directed path from u to v OR from v to u (or both).
# Output 1 if semi-connected, -1 otherwise. Multiple test cases.
#
# Algorithm:
#   1. Find strongly connected components (Kosaraju's or Tarjan's).
#   2. Build the DAG of SCCs.
#   3. The original graph is semi-connected iff the condensed DAG has a
#      Hamiltonian path, which holds iff the topological order of the DAG
#      has edges between every consecutive pair.

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_sc.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def kosaraju(n, adj, radj):
    """Return list of SCCs using Kosaraju's two-pass algorithm."""
    visited = [False] * (n + 1)
    order = []

    def dfs1(u):
        stack = [(u, False)]
        while stack:
            v, done = stack.pop()
            if done:
                order.append(v)
                continue
            if visited[v]:
                continue
            visited[v] = True
            stack.append((v, True))
            for nb in adj[v]:
                if not visited[nb]:
                    stack.append((nb, False))

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * (n + 1)
    num_comp = 0

    def dfs2(u, c):
        stack = [u]
        while stack:
            v = stack.pop()
            if comp[v] != -1:
                continue
            comp[v] = c
            for nb in radj[v]:
                if comp[nb] == -1:
                    stack.append(nb)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, num_comp)
            num_comp += 1

    return comp, num_comp

def is_semi_connected(n, adj):
    radj = defaultdict(list)
    for u in adj:
        for v in adj[u]:
            radj[v].append(u)

    comp, num_comp = kosaraju(n, adj, radj)

    # Build condensed DAG
    cond_adj = defaultdict(set)
    cond_in = defaultdict(int)
    for c in range(num_comp):
        cond_in[c]
    for u in range(1, n + 1):
        for v in adj[u]:
            if comp[u] != comp[v]:
                if comp[v] not in cond_adj[comp[u]]:
                    cond_adj[comp[u]].add(comp[v])
                    cond_in[comp[v]] += 1

    # Topological order of condensed DAG (Kahn's)
    queue = deque(c for c in range(num_comp) if cond_in[c] == 0)
    topo = []
    temp_in = dict(cond_in)
    while queue:
        c = queue.popleft()
        topo.append(c)
        for nb in cond_adj[c]:
            temp_in[nb] -= 1
            if temp_in[nb] == 0:
                queue.append(nb)

    # Check Hamiltonian path in condensed DAG: every consecutive pair must have an edge
    for i in range(len(topo) - 1):
        if topo[i+1] not in cond_adj[topo[i]]:
            return False
    return True

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
        adj = defaultdict(list)
        for j in range(m):
            u, v = map(int, lines[i+1+j].split())
            adj[u].append(v)
        for node in range(1, n+1):
            if node not in adj:
                adj[node] = []
        results.append(1 if is_semi_connected(n, adj) else -1)
        i += m + 1
    print(' '.join(map(str, results)))

if __name__ == '__main__':
    solve(get_input())
