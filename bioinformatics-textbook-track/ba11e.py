# BA11E — Sequence a Peptide
# https://rosalind.info/problems/ba11e/
#
# Given: A spectral vector Spectral (space-separated integers of length n).
# Return: A peptide with maximum score against Spectral among all peptides
#         of parent mass n (i.e., whose prefix masses lie in [1, n]).
#
# We use dynamic programming on the spectral vector: dp[i] = best score
# achievable for a peptide of total mass i. Edges correspond to amino-acid
# mass steps between positions in the spectral vector.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba11e.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

AA_MASSES = sorted({
    57:'G', 71:'A', 87:'S', 97:'P', 99:'V', 101:'T', 103:'C',
    113:'L', 114:'N', 115:'D', 128:'Q', 129:'E', 131:'M',
    137:'H', 147:'F', 156:'R', 163:'Y', 186:'W'
}.items())
MASS_TO_AA = {m: aa for m, aa in AA_MASSES}
MASSES = [m for m, _ in AA_MASSES]

def solve(data):
    spectral = list(map(int, data.split()))
    n = len(spectral)
    # dp[i] = (best_score reaching position i, previous position, aa)
    dp = [(-float('inf'), -1, '') for _ in range(n + 1)]
    dp[0] = (0, -1, '')

    for j in range(1, n + 1):
        for m in MASSES:
            i = j - m
            if i < 0: continue
            if dp[i][0] == -float('inf'): continue
            score = dp[i][0] + spectral[j - 1]  # spectral is 0-indexed; position j is spectral[j-1]
            if score > dp[j][0]:
                dp[j] = (score, i, MASS_TO_AA[m])

    # Reconstruct
    peptide = []
    cur = n
    while dp[cur][1] != -1:
        peptide.append(dp[cur][2])
        cur = dp[cur][1]
    print(''.join(reversed(peptide)))

if __name__ == '__main__': solve(get_input())
