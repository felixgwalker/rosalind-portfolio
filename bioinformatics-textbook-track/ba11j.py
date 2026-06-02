# BA11J — Compute the Probability of a Spectral Dictionary
# https://rosalind.info/problems/ba11j/
#
# Given: A spectral vector Spectral, a score threshold T, a max mass m,
#        and amino acid probabilities (one per amino acid, same order as masses).
# Return: The probability that a randomly generated peptide of mass at most m
#         scores ≥ T against Spectral (i.e., Prob(Spectral Dictionary)).
#
# Same DP as BA11I but weights each path by the product of its amino acid
# probabilities instead of counting equally.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba11j.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

# Standard amino acid masses in the same order Rosalind uses for BA11J.
AA_MASSES = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def solve(data):
    lines = data.splitlines()
    spectral = list(map(int, lines[0].split()))
    T = int(lines[1].strip())
    max_mass = int(lines[2].strip())
    aa_probs = list(map(float, lines[3].split()))  # probability for each AA mass

    n = len(spectral)
    from collections import defaultdict
    # dp[j] maps score → total probability of paths reaching position j with that score
    dp = defaultdict(lambda: defaultdict(float))
    dp[0][0] = 1.0

    for j in range(1, min(n, max_mass) + 1):
        gain = spectral[j - 1]
        for idx, m in enumerate(AA_MASSES):
            prev_j = j - m
            if prev_j < 0: continue
            prob = aa_probs[idx]
            for score, p in dp[prev_j].items():
                dp[j][score + gain] += p * prob

    total_prob = 0.0
    for j in range(1, min(n, max_mass) + 1):
        for score, p in dp[j].items():
            if score >= T:
                total_prob += p

    print(f"{total_prob:.4f}")

if __name__ == '__main__': solve(get_input())
