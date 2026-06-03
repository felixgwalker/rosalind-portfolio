# Square in a Graph (SQ)
# Rosalind problem: https://rosalind.info/problems/sq/
#
# Problem: Given an undirected graph, determine if it contains a square
# (a cycle of length exactly 4). Output 1 if yes, -1 if no.
# Multiple test cases may be given.
#
# Algorithm: For each pair of nodes (u, v) that are not adjacent, check if they
# have at least 2 common neighbours — that would form a square u-a-v-b-u.
# O(n³) in the worst case.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_sq.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def has_square(n, adj):
    neighbours = {i: set(adj[i]) for i in range(1, n+1)}
    for u in range(1, n+1):
        for v in range(u+1, n+1):
            # Check if u and v have >= 2 common neighbours
            common = neighbours[u] & neighbours[v]
            if len(common) >= 2:
                return True
    return False

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
            adj[v].append(u)
        results.append('1' if has_square(n, adj) else '-1')
        i += m + 1
    print(' '.join(results))

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
