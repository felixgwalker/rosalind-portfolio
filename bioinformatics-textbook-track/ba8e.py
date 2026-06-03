# BA8E — Implement Hierarchical Clustering
# https://rosalind.info/problems/ba8e/
#
# Given: integer n and an n×n distance matrix.
# Return: a dendrogram via hierarchical clustering (UPGMA-like merging).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba8e.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    D = [list(map(float, l.split())) for l in lines[1:n+1] if l.strip()]
    clusters = [[i+1] for i in range(n)]
    dist = {(i,j): D[i][j] for i in range(n) for j in range(n)}

    def cluster_dist(a, b):
        total = sum(D[i-1][j-1] for i in clusters[a] for j in clusters[b])
        return total / (len(clusters[a]) * len(clusters[b]))

    active = list(range(n))
    while len(active) > 1:
        best_d = float('inf'); best_i = best_j = 0
        for ii in range(len(active)):
            for jj in range(ii+1, len(active)):
                d = cluster_dist(active[ii], active[jj])
                if d < best_d: best_d, best_i, best_j = d, active[ii], active[jj]
        merged = sorted(clusters[best_i] + clusters[best_j])
        print(' '.join(map(str, merged)))
        clusters.append(merged)
        new_idx = len(clusters)-1
        active.remove(best_i); active.remove(best_j); active.append(new_idx)
        # Update D for new cluster
        for k in active:
            if k != new_idx:
                pass   # computed on-the-fly via cluster_dist

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
