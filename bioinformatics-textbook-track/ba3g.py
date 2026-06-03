# BA3G — Find an Eulerian Path in a Graph
# https://rosalind.info/problems/ba3g/
#
# Given: a directed graph with exactly one node with out-degree > in-degree (start)
# and one node with in-degree > out-degree (end).
# Return: an Eulerian path (visits every edge exactly once).
#
# Algorithm: Add a virtual edge from end→start, find Eulerian cycle, then
# rotate the cycle to start at the real start node.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3g.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def eulerian_cycle(graph):
    start = next(iter(graph))
    stack, circuit = [start], []
    while stack:
        v = stack[-1]
        if graph.get(v):
            stack.append(graph[v].pop())
        else:
            circuit.append(stack.pop())
    return circuit[::-1]

def solve(data):
    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    nodes = set()
    for line in data.splitlines():
        if not line.strip():
            continue
        left, right = line.split(' -> ')
        u = left.strip()
        neighbors = right.strip().split(',')
        graph[u].extend(neighbors)
        out_deg[u] += len(neighbors)
        for v in neighbors:
            in_deg[v] += 1
            nodes.update([u, v])

    # Find start (out > in) and end (in > out)
    start = end = None
    for node in nodes:
        diff = out_deg[node] - in_deg[node]
        if diff == 1:
            start = node
        elif diff == -1:
            end = node

    # Add virtual edge end → start to make it Eulerian
    graph[end].append(start)
    cycle = eulerian_cycle(graph)

    # Find the virtual edge in the cycle and rotate
    for i in range(len(cycle) - 1):
        if cycle[i] == end and cycle[i+1] == start:
            path = cycle[i+1:] + cycle[1:i+1]
            print('->'.join(path))
            return

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
