# BA5I — Find a Highest-Scoring Overlap Alignment
# https://rosalind.info/problems/ba5i/
#
# Given: two strings s and t. Find the highest-scoring overlap alignment:
# a suffix of s aligned with a prefix of t.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba5i.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines(); s, t = lines[0].strip(), lines[1].strip()
    m, n = len(s), len(t)
    GAP, MATCH, MISMATCH = -2, 1, -2
    dp = [[0]*(n+1) for _ in range(m+1)]
    for j in range(1, n+1): dp[0][j] = GAP*j
    for i in range(1, m+1):
        for j in range(1, n+1):
            sc = MATCH if s[i-1]==t[j-1] else MISMATCH
            dp[i][j] = max(dp[i-1][j-1]+sc, dp[i-1][j]+GAP, dp[i][j-1]+GAP)
    best = max(dp[i][n] for i in range(m+1))
    print(best)

if __name__ == '__main__': solve(get_input())
