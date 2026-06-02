# BA5B — Find the Length of a Longest Path in a Manhattan-like Grid
# https://rosalind.info/problems/ba5b/
#
# Given: integers n and m, and two matrices of edge weights (down-edges, right-edges).
# Return: the length of the longest path from (0,0) to (n,m) in a grid DAG.
# DP: dp[i][j] = max(dp[i-1][j]+down[i-1][j], dp[i][j-1]+right[i][j-1]).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba5b.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    # n+1 rows, m cols of down edges; then separator; then n rows, m+1 cols of right edges
    down = []
    i = 1
    while len(down) < n:
        row = list(map(int, lines[i].split()))
        down.append(row)
        i += 1
    i += 1  # skip separator '-'
    right = []
    while len(right) < n + 1 and i < len(lines):
        row = list(map(int, lines[i].split()))
        right.append(row)
        i += 1

    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] + right[0][j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j] + down[i-1][j], dp[i][j-1] + right[i][j-1])
    print(dp[n][m])

if __name__ == '__main__': solve(get_input())
