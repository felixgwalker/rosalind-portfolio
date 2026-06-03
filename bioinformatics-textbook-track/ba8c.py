# BA8C — Implement the Lloyd Algorithm for k-Means Clustering
# https://rosalind.info/problems/ba8c/
#
# Given: integers k and m, and a set of data points.
# Return: k centers after running Lloyd's k-means algorithm until convergence.

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba8c.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def dist(a, b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

def solve(data):
    lines = data.splitlines()
    k, m = map(int, lines[0].split())
    points = [list(map(float, l.split())) for l in lines[1:] if l.strip()]
    # Initialize with first k points
    centers = [points[i][:] for i in range(k)]
    for _ in range(1000):
        # Assign each point to nearest center
        clusters = [[] for _ in range(k)]
        for p in points:
            nearest = min(range(k), key=lambda i: dist(p, centers[i]))
            clusters[nearest].append(p)
        # Update centers
        new_centers = []
        for i in range(k):
            if clusters[i]:
                new_centers.append([sum(p[j] for p in clusters[i])/len(clusters[i]) for j in range(m)])
            else:
                new_centers.append(centers[i])
        if all(dist(new_centers[i], centers[i]) < 1e-10 for i in range(k)):
            break
        centers = new_centers
    for c in centers:
        print(' '.join(f'{x:.3f}' for x in c))

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
