# BA8D — Implement the Soft k-Means Clustering Algorithm
# https://rosalind.info/problems/ba8d/
#
# Given: integers k and m, β (stiffness), and a set of points.
# Return: k centers after soft k-means EM convergence.

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba8d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def dist2(a, b):
    return sum((x-y)**2 for x,y in zip(a,b))

def solve(data):
    lines = data.splitlines()
    k, m = map(int, lines[0].split())
    beta = float(lines[1].strip())
    points = [list(map(float, l.split())) for l in lines[2:] if l.strip()]
    n = len(points)
    centers = [points[i][:] for i in range(k)]
    for _ in range(100):
        # E-step: compute soft assignments
        hidden = []
        for p in points:
            weights = [math.exp(-beta * dist2(p, c)) for c in centers]
            total = sum(weights)
            hidden.append([w/total for w in weights])
        # M-step: update centers
        new_centers = []
        for j in range(k):
            total_w = sum(hidden[i][j] for i in range(n))
            if total_w < 1e-10: new_centers.append(centers[j][:]); continue
            new_c = [sum(hidden[i][j]*points[i][d] for i in range(n))/total_w for d in range(m)]
            new_centers.append(new_c)
        if all(dist2(new_centers[j], centers[j]) < 1e-12 for j in range(k)): break
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
