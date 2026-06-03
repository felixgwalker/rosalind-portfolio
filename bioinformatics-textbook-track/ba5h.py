# BA5H — Find a Highest-Scoring Fitting Alignment
# https://rosalind.info/problems/ba5h/
#
# Given: two strings s and t. Find the highest-scoring fitting alignment:
# align t against a substring of s (no gap penalty at start/end of s).
# Score: match=1, mismatch=-1, gap=-1.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba5h.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines(); s, t = lines[0].strip(), lines[1].strip()
    m, n = len(s), len(t)
    GAP, MATCH, MISMATCH = -1, 1, -1
    # Free leading gaps in s (row 0 = 0)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for j in range(1, n+1): dp[0][j] = GAP*j  # penalise gaps in t
    # Free trailing gaps in s: first column stays 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            sc = MATCH if s[i-1]==t[j-1] else MISMATCH
            dp[i][j] = max(dp[i-1][j-1]+sc, dp[i-1][j]+GAP, dp[i][j-1]+GAP)
    # Best score in last column (free trailing s gap)
    best_score = max(dp[i][n] for i in range(m+1))
    print(best_score)

if __name__ == '__main__':
    import io, contextlib
    data, out_path = get_input()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        solve(data)
    output = buf.getvalue()
    sys.stdout.write(output)
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(output)
