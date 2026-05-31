# Searching a Graph with a Sink (RDAG)
# Rosalind problem: https://rosalind.info/problems/rdag/
#
# Problem: Given a directed acyclic graph (DAG), find a node that has a
# directed path to every other node in the graph. This node is called a
# "general sink" (or source, depending on edge direction convention).
# If no such node exists, print -1.
#
# Algorithm: Topological sort. In a DAG, if a node v has paths to all other
# nodes, it must be the LAST node in the topological order (a sink). Check the
# last topologically-sorted node: if it can reach all others via reverse BFS, print it.

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_rdag.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    # Input: first line is number of nodes, then edges
    n = int(lines[0])
    adj = defaultdict(list)       # forward edges
    in_degree = defaultdict(int)
    nodes = set(range(1, n + 1))

    for line in lines[1:]:
        parts = line.split()
        if len(parts) >= 2:
            u, v = int(parts[0]), int(parts[1])
            adj[u].append(v)
            in_degree[v] += 1

    # Kahn's topological sort
    queue = deque(node for node in nodes if in_degree[node] == 0)
    topo = []
    temp_in = dict(in_degree)
    while queue:
        u = queue.popleft()
        topo.append(u)
        for v in adj[u]:
            temp_in[v] -= 1
            if temp_in[v] == 0:
                queue.append(v)

    if not topo:
        print(-1)
        return

    # The candidate is the last node in topological order
    candidate = topo[-1]

    # Verify: does candidate have a path to ALL nodes (via reverse graph BFS)?
    rev_adj = defaultdict(list)
    for u in adj:
        for v in adj[u]:
            rev_adj[v].append(u)

    # BFS backward from candidate
    visited = {candidate}
    queue = deque([candidate])
    while queue:
        v = queue.popleft()
        for u in rev_adj[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)

    if visited == nodes:
        print(candidate)
    else:
        print(-1)

if __name__ == '__main__':
    solve(get_input())
