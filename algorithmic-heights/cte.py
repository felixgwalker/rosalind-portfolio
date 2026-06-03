# Shortest Cycle Through a Given Edge (CTE)
# Rosalind problem: https://rosalind.info/problems/cte/
#
# Problem: Given a weighted directed graph and k query edges (u, v), for each
# query find the length of the shortest cycle that uses the edge u→v.
# The cycle length equals weight(u→v) + dist(v, u) via Dijkstra from v.
# Output -1 if no cycle through that edge exists.
# Algorithm: Dijkstra from each query edge's target. O(k(n+m) log n).

import os
import sys
import heapq
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_cte.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def dijkstra(adj, src, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    edge_weight = {}
    for line in lines[1:m+1]:
        u, v, w = map(int, line.split())
        adj[u].append((v, w))
        if (u, v) not in edge_weight or w < edge_weight[(u, v)]:
            edge_weight[(u, v)] = w

    k = int(lines[m+1])
    results = []
    for line in lines[m+2:m+2+k]:
        u, v = map(int, line.split())
        w = edge_weight.get((u, v), float('inf'))
        dist = dijkstra(adj, v, n)
        if dist[u] == float('inf') or w == float('inf'):
            results.append('-1')
        else:
            results.append(str(int(w + dist[u])))
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
