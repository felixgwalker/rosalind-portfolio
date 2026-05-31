# Independent Alleles (LIA)
# Rosalind problem: https://rosalind.info/problems/lia/
#
# Problem: Two Aa Bb organisms mate. After k generations of always crossing
# with Aa Bb (so every individual is Aa Bb × Aa Bb), we have 2^k individuals
# in generation k+1. Return the probability that at least n of them are Aa Bb.
#
# Key insight: Mendel's second law — loci on different chromosomes segregate
# independently. P(offspring is Aa) = 1/2, P(offspring is Bb) = 1/2, so
# P(AaBb) = 1/4 independently for each organism.
#
# Algorithm: Binomial distribution — X ~ Binomial(2^k, 1/4).
# P(X ≥ n) = Σ_{i=n}^{2^k} C(2^k, i) * (1/4)^i * (3/4)^(2^k - i)

import os
import sys
from math import comb

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_lia.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    k, n = map(int, data.split())
    N = 2 ** k          # total offspring in generation k+1
    p = 0.25            # P(AaBb) per individual

    # Sum tail of binomial CDF from n to N
    prob = sum(comb(N, i) * (p ** i) * ((1 - p) ** (N - i)) for i in range(n, N + 1))
    print(round(prob, 3))

if __name__ == '__main__':
    solve(get_input())
