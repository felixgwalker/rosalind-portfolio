# Shortest Paths in DAG (SDAG)
# Rosalind problem: https://rosalind.info/problems/sdag/
#
# Problem: Given a weighted DAG, find the shortest path from node 1 to all
# other nodes. Output each distance or "x" if unreachable.
#
# Algorithm: Topological sort + single-source shortest paths by relaxing edges
# in topological order. O(n + m) — more efficient than Dijkstra for DAGs.

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_sdag.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    in_degree = {i: 0 for i in range(1, n+1)}
    for line in lines[1:m+1]:
        u, v, w = map(int, line.split())
        adj[u].append((v, w))
        in_degree[v] += 1

    # Kahn's topological sort
    queue = deque(node for node in range(1, n+1) if in_degree[node] == 0)
    topo = []
    temp_in = dict(in_degree)
    while queue:
        u = queue.popleft()
        topo.append(u)
        for v, _ in adj[u]:
            temp_in[v] -= 1
            if temp_in[v] == 0:
                queue.append(v)

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0

    for u in topo:
        if dist[u] == INF:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    print(' '.join(str(dist[i]) if dist[i] != INF else 'x' for i in range(1, n+1)))

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
