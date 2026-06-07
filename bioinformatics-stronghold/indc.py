# Independent Segregation of Chromosomes (INDC)
# Rosalind problem: https://rosalind.info/problems/indc/
#
# Problem: Given a positive integer n (≤ 50) of chromosome pairs, two diploid
# siblings each receive 2n chromosomes total (one homolog from each of the n
# pairs from each parent). For each of these 2n parental chromosomes, both
# siblings independently inherit one of two homologs, so they share it with
# probability 1/2. Compute P(siblings share at least k of their 2n chromosomes)
# for k = 1 to 2n. Output the 2n log₁₀ probabilities.
#
# Model: M ~ Binomial(2n, 1/2).
# P(M ≥ k) = Σ_{i=k}^{2n} C(2n, i) * (1/2)^(2n)

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
    total = 2 * n
    results = []
    # For k from 1 to 2n: P(M >= k) where M ~ Bin(2n, 0.5)
    for k in range(1, total + 1):
        prob = sum(comb(total, i) for i in range(k, total + 1)) / (2 ** total)
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
