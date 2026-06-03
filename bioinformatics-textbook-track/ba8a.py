# BA8A — Implement FarthestFirstTraversal
# https://rosalind.info/problems/ba8a/
#
# Given: integers k (clusters) and m (dimensions), and a set of points.
# Return: k centers produced by FarthestFirstTraversal.

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba8a.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def dist(a, b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

def solve(data):
    lines = data.splitlines()
    k, m = map(int, lines[0].split())
    points = [list(map(float, l.split())) for l in lines[1:] if l.strip()]
    centers = [points[0]]
    for _ in range(k-1):
        farthest = max(points, key=lambda p: min(dist(p,c) for c in centers))
        centers.append(farthest)
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
