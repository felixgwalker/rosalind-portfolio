# Longest Path in a DAG (LONG)
# Rosalind problem: https://rosalind.info/problems/long/
#   (Not to be confused with the Stronghold's shortest superstring problem.)
#
# Problem: Given a weighted DAG, find the length of the longest path.
# Output: The maximum path length.
#
# Algorithm: Topological sort + DP relaxation. O(n + m).

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_long.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    adj = defaultdict(list)
    in_degree = {i: 0 for i in range(1, n+1)}
    for line in lines[1:m+1]:
        u, v, w = map(int, line.split())
        adj[u].append((v, w))
        in_degree[v] += 1

    # Topological sort
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

    # DP for longest path
    dist = {i: 0 for i in range(1, n+1)}
    for u in topo:
        for v, w in adj[u]:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w

    print(max(dist.values()))

if __name__ == '__main__':
    solve(get_input())
