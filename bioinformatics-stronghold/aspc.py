# Introduction to Alternative Splicing (ASPC)
# Rosalind problem: https://rosalind.info/problems/aspc/
#
# Problem: Given integers n (total exons, ≤ 50) and m (minimum exons to keep),
# return the number of ways to choose at least m exons from n, modulo 1,000,000.
# This models alternative splicing: each subset of ≥ m exons can form a distinct
# mRNA isoform (ignoring ordering, as exon order is fixed in the genome).
#
# Formula: sum_{k=m}^{n} C(n, k)  mod  1,000,000

import os
import sys
from math import comb

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_aspc.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MOD = 1_000_000

def solve(data):
    n, m = map(int, data.split())
    total = sum(comb(n, k) for k in range(m, n + 1)) % MOD
    print(total)

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
