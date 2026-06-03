# Hamiltonian Path in DAG (HDAG)
# Rosalind problem: https://rosalind.info/problems/hdag/
#
# Problem: Given a DAG, determine if a Hamiltonian path exists (a path visiting
# every node exactly once). If so, output 1 and the path; otherwise output -1.
# Multiple test cases may be given.
#
# Algorithm: A Hamiltonian path exists in a DAG iff there is a unique topological
# ordering (each consecutive pair in the ordering is connected by an edge).
# Compute the topological sort via Kahn's and verify consecutiveness. O(n + m).

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_hdag.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def hamiltonian_dag(n, edges):
    adj = defaultdict(set)
    in_degree = {i: 0 for i in range(1, n+1)}
    for u, v in edges:
        adj[u].add(v)
        in_degree[v] += 1

    # Kahn's topo sort; a Hamiltonian path requires each step to have exactly 1 choice
    queue = deque(node for node in range(1, n+1) if in_degree[node] == 0)
    if len(queue) != 1:
        return None   # multiple roots → no unique Ham. path
    topo = []
    temp_in = dict(in_degree)
    while queue:
        if len(queue) > 1:
            return None
        u = queue.popleft()
        topo.append(u)
        for v in adj[u]:
            temp_in[v] -= 1
            if temp_in[v] == 0:
                queue.append(v)

    if len(topo) != n:
        return None   # cycle or not all nodes reached

    # Verify each consecutive pair has an edge
    for i in range(len(topo) - 1):
        if topo[i+1] not in adj[topo[i]]:
            return None

    return topo

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
        path = hamiltonian_dag(n, edges)
        if path:
            results.append('1')
            results.append(' '.join(map(str, path)))
        else:
            results.append('-1')
        i += m + 1
    print('\n'.join(results))

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
