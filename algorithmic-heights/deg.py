# Degree Array (DEG)
# Rosalind problem: https://rosalind.info/problems/deg/
#
# Problem: Given an undirected graph, output the degree sequence — the degree
# of each node in order 1..n. The degree of a node is the number of edges
# incident to it.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_deg.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    degree = defaultdict(int)
    for line in lines[1:m+1]:
        u, v = map(int, line.split())
        degree[u] += 1
        degree[v] += 1
    print(' '.join(str(degree[i]) for i in range(1, n+1)))

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
