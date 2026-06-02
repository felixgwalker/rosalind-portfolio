# BA3M — Generate All Maximal Non-Branching Paths in a Graph
# https://rosalind.info/problems/ba3m/
#
# Given: An adjacency list for a graph G.
# Return: All maximal non-branching paths in G.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3m.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    graph = defaultdict(list)

    for line in data.splitlines():
        line = line.strip()
        if not line: continue
        left, right = line.split(' -> ')
        u = int(left.strip())
        neighbors = [int(x.strip()) for x in right.strip().split(',')]
        graph[u].extend(neighbors)
        out_deg[u] += len(neighbors)
        for v in neighbors:
            in_deg[v] += 1

    all_nodes = set(graph.keys()) | set(in_deg.keys())
    visited_edges = set()
    paths = []

    for u in sorted(all_nodes):
        if not (in_deg[u] == 1 and out_deg[u] == 1):
            for v in graph.get(u, []):
                if (u, v) not in visited_edges:
                    path = [u, v]
                    visited_edges.add((u, v))
                    w = v
                    while in_deg[w] == 1 and out_deg[w] == 1:
                        nxt = graph[w][0]
                        visited_edges.add((w, nxt))
                        path.append(nxt)
                        w = nxt
                    paths.append(path)

    # Isolated cycles: every node on the cycle is 1-in-1-out
    for u in sorted(all_nodes):
        if in_deg[u] == 1 and out_deg[u] == 1:
            for v in graph.get(u, []):
                if (u, v) not in visited_edges:
                    cycle = [u]
                    visited_edges.add((u, v))
                    w = v
                    while w != u:
                        cycle.append(w)
                        nxt = graph[w][0]
                        visited_edges.add((w, nxt))
                        w = nxt
                    cycle.append(u)
                    paths.append(cycle)

    for path in paths:
        print(' -> '.join(map(str, path)))

if __name__ == '__main__': solve(get_input())
