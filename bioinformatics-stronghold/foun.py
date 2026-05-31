# The Founder Effect and Genetic Drift (FOUN)
# Rosalind problem: https://rosalind.info/problems/foun/
#
# Problem: Given a population of N diploid individuals, an allele that appears
# in m copies initially (out of 2N total alleles), and g generations of drift,
# compute the probability that the allele is LOST (fixed at 0) in each generation
# from 1 to g. Output g log₁₀ probabilities.
#
# The Wright-Fisher model: allele frequency changes each generation by random
# sampling. P(k copies in gen t+1 | j copies in gen t) = C(2N,k)*(j/2N)^k*(1-j/2N)^(2N-k).
# We track the probability distribution across all possible allele counts and
# accumulate P(count == 0) each generation.

import os
import sys
import math
from math import comb, log10

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_foun.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    N, m, g = map(int, lines[0].split())
    total = 2 * N

    # Initial distribution: exactly m copies
    # dp[k] = probability of having k copies of the allele
    dp = [0.0] * (total + 1)
    dp[m] = 1.0

    results = []
    for _ in range(g):
        new_dp = [0.0] * (total + 1)
        for j in range(total + 1):
            if dp[j] == 0.0:
                continue
            p = j / total   # current allele frequency
            for k in range(total + 1):
                # Binomial transition probability
                try:
                    binom = comb(total, k) * (p ** k) * ((1 - p) ** (total - k))
                except:
                    binom = 0.0
                new_dp[k] += dp[j] * binom
        dp = new_dp
        # P(lost) = P(0 copies)
        lost = dp[0]
        if lost > 0:
            results.append(round(log10(lost), 3))
        else:
            results.append(-float('inf'))   # essentially impossible

    print(' '.join(map(str, results)))

if __name__ == '__main__':
    solve(get_input())
