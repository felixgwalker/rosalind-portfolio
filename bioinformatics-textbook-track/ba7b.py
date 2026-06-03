# BA7B — Implement LIMB Length Problem
# https://rosalind.info/problems/ba7b/
#
# Given: integer n, leaf j, and n×n distance matrix D.
# Return: the limb length of leaf j in the unique additive tree for D.
# LimbLength(j) = min over all i,k ≠ j of (D[i][j] + D[j][k] - D[i][k]) / 2.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba7b.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n, j = int(lines[0].strip()), int(lines[1].strip())
    D = [list(map(int, l.split())) for l in lines[2:n+2] if l.strip()]
    best = float('inf')
    for i in range(n):
        for k in range(n):
            if i != j and k != j and i != k:
                limb = (D[i][j] + D[j][k] - D[i][k]) / 2
                if limb < best: best = limb
    print(int(best))

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
