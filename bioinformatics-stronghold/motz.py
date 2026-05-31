# Motzkin Numbers and RNA Secondary Structures (MOTZ)
# Rosalind problem: https://rosalind.info/problems/motz/
#
# Problem: Given an RNA string s (in FASTA format), count the number of
# noncrossing partial matchings of basepair edges — i.e., secondary structures
# where some bases may be unpaired (unlike CAT, which required perfect matchings).
# Return the result modulo 1,000,000.
#
# Algorithm: Interval DP, similar to CAT but s[i] may now be left unmatched.
#   dp[i][j] = number of noncrossing partial matchings for s[i..j]
#   Empty interval: 1 (one way to match nothing).
#   Recurrence: s[i] is either
#     1. Unmatched: contributes dp[i+1][j]
#     2. Paired with s[k] for any k in [i+1, j] where (s[i],s[k]) are complementary:
#        contributes dp[i+1][k-1] * dp[k+1][j]
#   O(n³) time.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_motz.txt')
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

PAIRS = {('A','U'), ('U','A'), ('G','C'), ('C','G')}
MOD = 1_000_000

def solve(data):
    s = parse_fasta(data)
    n = len(s)

    # dp[i][j]: noncrossing partial matchings for s[i..j]
    # We use memoisation via a 2D table filled by interval length.
    dp = [[0] * n for _ in range(n)]

    # Base: single-character intervals — 1 way (leave unmatched)
    for i in range(n):
        dp[i][i] = 1

    # Helper: dp value for empty interval (i > j) = 1
    def get(i, j):
        if i > j:
            return 1
        return dp[i][j]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Option 1: s[i] is unmatched
            val = get(i + 1, j)
            # Option 2: s[i] pairs with s[k] for each valid k
            for k in range(i + 1, j + 1):
                if (s[i], s[k]) in PAIRS:
                    val = (val + get(i+1, k-1) * get(k+1, j)) % MOD
            dp[i][j] = val

    print(get(0, n - 1))

if __name__ == '__main__':
    solve(get_input())
