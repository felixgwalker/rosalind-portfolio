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
                        '..', 'rosalind-files', 'rosalind_afrq.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

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
    solve(get_input())
