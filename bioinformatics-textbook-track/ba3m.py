# BA3M — Generate All Maximal Non-Branching Paths in a Graph
# https://rosalind.info/problems/ba3m/
#
# Given: An adjacency list for a graph G.
# Return: All maximal non-branching paths in G.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3m.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

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

if __name__ == '__main__':
    import io, contextlib
    data, out_path = get_input()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        solve(data)
    output = buf.getvalue()
    sys.stdout.write(output)
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(output)
