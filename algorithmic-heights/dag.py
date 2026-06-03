# Testing Acyclicity (DAG)
# Rosalind problem: https://rosalind.info/problems/dag/
#
# Problem: Given a directed graph, determine whether it is a DAG (directed
# acyclic graph). Output 1 if it is acyclic, -1 if it contains a cycle.
# Multiple test cases may be given.
#
# Algorithm: Topological sort (Kahn's). If we process all n nodes, it's a DAG;
# if some remain unprocessed (stuck in a cycle), it's cyclic.

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_dag.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def is_dag(n, edges):
    adj = defaultdict(list)
    in_degree = defaultdict(int)
    for node in range(1, n+1):
        in_degree[node]   # ensure all nodes are in the dict
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    queue = deque(node for node in range(1, n+1) if in_degree[node] == 0)
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return count == n   # if all nodes processed, no cycle

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
        edges = []
        for j in range(m):
            u, v = map(int, lines[i+1+j].split())
            edges.append((u, v))
        results.append(1 if is_dag(n, edges) else -1)
        i += m + 1
    print(' '.join(map(str, results)))

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
