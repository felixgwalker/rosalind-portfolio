# Counting Disease Carriers (AFRQ)
# Rosalind problem: https://rosalind.info/problems/afrq/
#
# Problem: Given an array of frequencies of a recessive disease allele in a
# population at Hardy-Weinberg equilibrium, for each allele frequency q,
# compute the proportion of heterozygous carriers (Aa genotype).
#
# Under Hardy-Weinberg:
#   P(AA) = (1-q)²,  P(Aa) = 2q(1-q),  P(aa) = q²
# where q is the recessive allele frequency.
#
# However, the problem gives the frequency of the homozygous recessive (aa),
# so we first compute q = sqrt(P(aa)), then P(Aa) = 2q(1-q).

import os
import sys
import math

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_afrq.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    freqs = list(map(float, data.split()))
    results = []
    for f in freqs:
        # f = P(aa) = q²  →  q = sqrt(f)
        q = math.sqrt(f)
        carrier = 2 * q * (1 - q)   # P(Aa) = 2q(1-q)
        results.append(round(carrier, 3))
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
