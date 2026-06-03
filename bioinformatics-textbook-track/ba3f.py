# BA3F — Find an Eulerian Cycle in a Graph
# https://rosalind.info/problems/ba3f/
#
# Given: a directed graph (adjacency list).
# Return: an Eulerian cycle (visits every edge exactly once).
#
# Algorithm: Hierholzer's algorithm. O(n + m).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3f.txt')
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
    for line in data.splitlines():
        if not line.strip():
            continue
        left, right = line.split(' -> ')
        graph[left.strip()].extend(right.strip().split(','))
    cycle = eulerian_cycle(graph)
    print('->'.join(cycle[:-1]))   # last node == first for a cycle

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
