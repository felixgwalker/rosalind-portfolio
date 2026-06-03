# BA7E — Implement Neighbor Joining
# https://rosalind.info/problems/ba7e/
#
# Given: integer n and an n×n distance matrix.
# Return: the unrooted tree produced by Neighbor Joining.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba7e.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    D = [list(map(float, l.split())) for l in lines[1:n+1] if l.strip()]
    labels = list(range(n))
    adj = defaultdict(list)
    next_node = n

    def neighbor_joining_step(D, labels):
        n = len(D)
        if n == 2:
            u, v = labels[0], labels[1]
            adj[u].append((v, D[0][1])); adj[v].append((u, D[0][1]))
            return
        # Compute total distances
        totals = [sum(D[i]) for i in range(n)]
        # Compute D* (neighbor joining matrix)
        best = float('inf'); best_i = best_j = 0
        for i in range(n):
            for j in range(i+1, n):
                d_star = (n-2)*D[i][j] - totals[i] - totals[j]
                if d_star < best: best, best_i, best_j = d_star, i, j
        # Compute branch lengths
        w_i = D[best_i][best_j]/2 + (totals[best_i]-totals[best_j])/(2*(n-2))
        w_j = D[best_i][best_j] - w_i
        new_node = next_node; next_node.__class__
        # Use a mutable counter
        nonlocal _next
        new_node = _next[0]; _next[0] += 1
        adj[new_node].append((labels[best_i], w_i)); adj[labels[best_i]].append((new_node, w_i))
        adj[new_node].append((labels[best_j], w_j)); adj[labels[best_j]].append((new_node, w_j))
        # New distance matrix (remove i and j, add new node)
        new_D = []; new_labels = []
        for k in range(n):
            if k == best_i or k == best_j: continue
            new_labels.append(labels[k])
        new_labels.append(new_node)
        for k in range(n):
            if k == best_i or k == best_j: continue
            row = []
            for l in range(n):
                if l == best_i or l == best_j: continue
                row.append(D[k][l])
            row.append((D[k][best_i] + D[k][best_j] - D[best_i][best_j]) / 2)
            new_D.append(row)
        last_row = [(D[k][best_i]+D[k][best_j]-D[best_i][best_j])/2 for k in range(n) if k!=best_i and k!=best_j] + [0.0]
        new_D.append(last_row)
        neighbor_joining_step(new_D, new_labels)

    _next = [n]

    def nj(D, labels):
        n = len(D)
        if n == 2:
            u, v = labels[0], labels[1]
            adj[u].append((v, D[0][1])); adj[v].append((u, D[0][1]))
            return
        totals = [sum(D[i]) for i in range(n)]
        best = float('inf'); best_i = best_j = 0
        for i in range(n):
            for j in range(i+1, n):
                d_star = (n-2)*D[i][j] - totals[i] - totals[j]
                if d_star < best: best, best_i, best_j = d_star, i, j
        w_i = D[best_i][best_j]/2 + (totals[best_i]-totals[best_j])/(2*(n-2))
        w_j = D[best_i][best_j] - w_i
        new_node = _next[0]; _next[0] += 1
        adj[new_node].append((labels[best_i], w_i)); adj[labels[best_i]].append((new_node, w_i))
        adj[new_node].append((labels[best_j], w_j)); adj[labels[best_j]].append((new_node, w_j))
        new_labels = [labels[k] for k in range(n) if k not in (best_i, best_j)] + [new_node]
        new_D = []
        for k in range(n):
            if k in (best_i, best_j): continue
            row = [D[k][l] for l in range(n) if l not in (best_i, best_j)]
            row.append((D[k][best_i]+D[k][best_j]-D[best_i][best_j])/2)
            new_D.append(row)
        last = [(D[k][best_i]+D[k][best_j]-D[best_i][best_j])/2 for k in range(n) if k not in (best_i, best_j)] + [0.0]
        new_D.append(last)
        nj(new_D, new_labels)

    nj(D, labels)
    for u in sorted(adj):
        for v, w in adj[u]:
            print(f"{u}->{v}:{w:.3f}")

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
