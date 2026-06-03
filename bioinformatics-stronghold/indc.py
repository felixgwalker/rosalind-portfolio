# Independent Segregation of Chromosomes (INDC)
# Rosalind problem: https://rosalind.info/problems/indc/
#
# Problem: Given a positive integer n (≤ 5), consider an organism with n pairs
# of chromosomes. When it produces a gamete, each chromosome is independently
# inherited from one of the two parents with probability 1/2.
#
# For a child with parents carrying alleles (n chromosome pairs), compute
# P(child inherits at least j of the n "special" chromosomes from one parent)
# for j = 1 to n. Output the n log₁₀ probabilities.
#
# Model: X ~ Binomial(n, 1/2).
# P(X ≥ j) = Σ_{k=j}^{n} C(n,k) * (1/2)^n

import os
import sys
import math
from math import comb, log10

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_indc.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    n = int(data.strip())
    results = []
    # For j from 1 to n: P(X >= j) where X ~ Bin(n, 0.5)
    for j in range(1, n + 1):
        prob = sum(comb(n, k) for k in range(j, n + 1)) / (2 ** n)
        results.append(round(log10(prob), 3))
    print(' '.join(map(str, results)))

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
