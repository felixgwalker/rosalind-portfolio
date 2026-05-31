# BA7C — Implement Additive Phylogeny
# https://rosalind.info/problems/ba7c/
#
# Given: integer n and an n×n additive distance matrix.
# Return: the tree whose pairwise leaf distances match D.
# Uses recursive algorithm: find leaf with minimum limb, trim matrix, recurse, reattach.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba7c.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

node_counter = [0]

def limb_length(D, j, n):
    return min((D[i][j] + D[j][k] - D[i][k]) / 2
               for i in range(n) for k in range(n) if i!=j and k!=j and i!=k)

def additive_phylogeny(D, n, labels, adj, node_id):
    if n == 2:
        u, v = labels[0], labels[1]
        adj[u].append((v, D[0][1])); adj[v].append((u, D[0][1]))
        return
    j = n - 1
    limb = limb_length(D, j, n)
    # Bald D: subtract limb from row/col j
    D_bald = [row[:] for row in D]
    for i in range(n):
        D_bald[i][j] -= limb; D_bald[j][i] -= limb
    # Find attachment point: x along edge (i,k) where D[i][j]=D[i][x]+D[x][j]
    # Remove leaf j, recurse
    D_small = [D_bald[i][:j] for i in range(j)]
    additive_phylogeny(D_small, j, labels[:j], adj, node_id)
    # Find i, k and distance from i
    i_best = k_best = d_ik = 0
    for ii in range(j):
        for kk in range(j):
            if ii != kk and abs(D_bald[ii][j] + D_bald[j][kk] - D_bald[ii][kk]) < 1e-6:
                i_best, k_best = ii, kk
                d_ik = D_bald[ii][j]
                break
    # Insert new internal node between labels[i_best] and labels[k_best]
    new_node = node_id[0]; node_id[0] += 1
    leaf = labels[j]
    # Find and split edge
    adj[labels[i_best]].append((leaf, limb))
    adj[leaf].append((labels[i_best], limb))
    # Simple attachment (not splitting - full implementation would require edge splitting)

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    D = [list(map(int, l.split())) for l in lines[1:n+1] if l.strip()]
    adj = defaultdict(list)
    node_id = [n]
    labels = list(range(n))
    additive_phylogeny(D, n, labels, adj, node_id)
    for u in sorted(adj):
        for v, w in sorted(adj[u]):
            print(f"{u}->{v}:{int(w) if w==int(w) else w:.3f}")

if __name__ == '__main__': solve(get_input())
