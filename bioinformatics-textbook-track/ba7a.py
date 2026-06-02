# BA7A — Compute Distances Between Leaves
# https://rosalind.info/problems/ba7a/
#
# Given: an integer n and an n×n additive distance matrix.
# Return: a weighted tree whose leaf-to-leaf distances match the matrix.
# Output: the tree as an adjacency list with edge weights, then the matrix.
# (This problem asks to reconstruct and output the additive tree.)

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba7a.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    # This problem asks: "Given a tree with weighted edges, output the n×n matrix
    # of distances between all leaf pairs." We assume the input is the tree adjacency list.
    lines = data.splitlines()
    n = int(lines[0].strip())
    from collections import defaultdict
    adj = defaultdict(list)
    for line in lines[1:]:
        line = line.strip()
        if not line: continue
        # Format: "u->v:weight"
        parts = line.split('->')
        u = int(parts[0].strip())
        v_w = parts[1].split(':')
        v, w = int(v_w[0].strip()), float(v_w[1].strip())
        adj[u].append((v, w)); adj[v].append((u, w))
    # BFS to compute all leaf-leaf distances
    from collections import deque
    leaves = [i for i in range(n)]
    result = [[0]*n for _ in range(n)]
    for src in leaves:
        dist = {src: 0}
        queue = deque([src])
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + w
                    queue.append(v)
        for tgt in leaves:
            result[src][tgt] = dist.get(tgt, 0)
    for row in result:
        print('\t'.join(str(int(x)) if x==int(x) else f'{x:.0f}' for x in row))

if __name__ == '__main__': solve(get_input())
