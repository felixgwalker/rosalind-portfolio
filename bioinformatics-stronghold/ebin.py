# Wright-Fisher's Model of Genetic Drift (EBIN)
# Rosalind problem: https://rosalind.info/problems/ebin/
#
# Problem: Given a population size N, and an allele frequency p among the
# founding population, compute the expected number of organisms in the
# FIRST generation that have 0, 1, 2, ..., 2N copies of the allele.
# Each diploid individual draws 2 alleles independently with probability p.
# So the number of copies per individual ~ Binomial(2, p).
#
# Expected count of individuals with k copies = N × C(2,k) × p^k × (1-p)^(2-k).

import os
import sys
from math import comb

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_ebin.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    N = int(lines[0].strip())
    p = float(lines[1].strip())

    # Each individual draws 2 alleles; possible copies: 0, 1, 2
    results = []
    for k in range(3):   # k = 0, 1, 2 copies
        expected = N * comb(2, k) * (p ** k) * ((1 - p) ** (2 - k))
        results.append(round(expected, 3))

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
