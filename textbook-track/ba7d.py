# BA7D — Implement UPGMA
# https://rosalind.info/problems/ba7d/
#
# Given: integer n and an n×n distance matrix.
# Return: the rooted tree produced by UPGMA (Unweighted Pair Group Method with Arithmetic Mean).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba7d.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    D = [list(map(float, l.split())) for l in lines[1:n+1] if l.strip()]
    # UPGMA: clusters start as individual leaves
    clusters = {i: [i] for i in range(n)}
    age = {i: 0.0 for i in range(n)}
    adj = defaultdict(list)
    next_node = n
    dist = {(i,j): D[i][j] for i in range(n) for j in range(n)}

    def cluster_dist(a, b):
        total = sum(dist.get((i,j), dist.get((j,i),0)) for i in clusters[a] for j in clusters[b])
        return total / (len(clusters[a]) * len(clusters[b]))

    active = set(range(n))
    while len(active) > 1:
        # Find minimum distance pair
        best_d = float('inf')
        best_i = best_j = -1
        active_list = sorted(active)
        for ii in range(len(active_list)):
            for jj in range(ii+1, len(active_list)):
                a, b = active_list[ii], active_list[jj]
                d = cluster_dist(a, b)
                if d < best_d: best_d, best_i, best_j = d, a, b
        new_age = best_d / 2
        new_node = next_node; next_node += 1
        age[new_node] = new_age
        w1 = new_age - age[best_i]; w2 = new_age - age[best_j]
        adj[new_node].append((best_i, w1)); adj[best_i].append((new_node, w1))
        adj[new_node].append((best_j, w2)); adj[best_j].append((new_node, w2))
        clusters[new_node] = clusters[best_i] + clusters[best_j]
        active.discard(best_i); active.discard(best_j); active.add(new_node)

    for u in sorted(adj):
        for v, w in adj[u]:
            print(f"{u}->{v}:{w:.3f}")

if __name__ == '__main__': solve(get_input())
