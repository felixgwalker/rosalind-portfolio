# Wobble Bonding and RNA Secondary Structures (RNAS)
# Rosalind problem: https://rosalind.info/problems/rnas/
#
# Problem: Given an RNA string s (in FASTA), count the total number of
# noncrossing partial matchings that include wobble base pairs (G-U / U-G)
# in addition to standard Watson-Crick pairs (A-U, U-A, G-C, C-G).
# Return the result modulo 1,000,000.
#
# This is identical to MOTZ but with an extended pair set that includes G↔U.
# Same interval DP approach: O(n³).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_rnas.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        if not line.startswith('>'):
            parts.append(line.strip())
    return ''.join(parts)

# Standard pairs + wobble G-U pairs
PAIRS = {('A','U'), ('U','A'), ('G','C'), ('C','G'), ('G','U'), ('U','G')}
MOD = 1_000_000

def solve(data):
    s = parse_fasta(data)
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    def get(i, j):
        if i > j:
            return 1
        return dp[i][j]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            val = get(i + 1, j)   # s[i] unmatched
            for k in range(i + 1, j + 1):
                if (s[i], s[k]) in PAIRS:
                    val = (val + get(i+1, k-1) * get(k+1, j)) % MOD
            dp[i][j] = val

    print(get(0, n - 1))

if __name__ == '__main__':
    solve(get_input())
