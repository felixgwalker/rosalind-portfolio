# The Wright-Fisher Model of Genetic Drift (WFMD)
# Rosalind problem: https://rosalind.info/problems/wfmd/
#
# Problem: Given population size N, initial allele count m, number of
# generations g, and a fixation threshold k, compute the probability that
# the allele reaches a count of at least k within g generations.
#
# Algorithm: Track the full probability distribution over allele counts 0..2N
# for g generations using the Wright-Fisher binomial sampling transition,
# then sum the probability of states ≥ k at any generation (first passage time).

import os
import sys
from math import comb

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_wfmd.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    N, m, g, k = map(int, data.split())
    total = 2 * N

    # dp[j] = probability of having j alleles
    dp = [0.0] * (total + 1)
    dp[m] = 1.0

    # Probability of reaching count >= k by generation g
    prob_reached = 0.0

    for _ in range(g):
        new_dp = [0.0] * (total + 1)
        for j in range(total + 1):
            if dp[j] == 0.0:
                continue
            p = j / total
            for i in range(total + 1):
                binom = comb(total, i) * (p ** i) * ((1 - p) ** (total - i))
                if i >= k:
                    prob_reached += dp[j] * binom
                else:
                    new_dp[i] += dp[j] * binom
        dp = new_dp

    print(round(prob_reached, 3))

if __name__ == '__main__':
    solve(get_input())
