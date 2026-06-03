# Finding Disjoint Motifs in a Gene (ITWV)
# Rosalind problem: https://rosalind.info/problems/itwv/
#
# Problem: Given strings t and u and a longer string s, determine whether t and
# u can be found as disjoint subsequences of s (each character of s can be used
# in at most one of t or u). Output a matrix: row i, col j = 1 if the i-th
# string and j-th string from input can be found as disjoint subsequences, 0 otherwise.
#
# Algorithm: 3D DP.
#   dp[i][j] = 1 iff we can match the first i chars of t and first j chars of u
#   using some prefix of s, with no overlap.
#   Transition (scanning s left to right):
#     dp2[i][j] = OR of:
#       dp[i][j]           (skip s[k] entirely)
#       dp[i-1][j]         if s[k] == t[i-1] (use s[k] for t)
#       dp[i][j-1]         if s[k] == u[j-1] (use s[k] for u)

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_itwv.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def can_interleave(s, t, u):
    """Check if t and u can be embedded as disjoint subsequences of s."""
    lt, lu = len(t), len(u)
    # dp[i][j] = True if we can embed t[0..i-1] and u[0..j-1] using some prefix of s
    dp = [[False] * (lu + 1) for _ in range(lt + 1)]
    dp[0][0] = True

    for ch in s:
        # Process in reverse to avoid using s[k] twice in the same step
        new_dp = [row[:] for row in dp]
        for i in range(lt + 1):
            for j in range(lu + 1):
                if not dp[i][j]:
                    continue
                if i < lt and ch == t[i]:
                    new_dp[i+1][j] = True
                if j < lu and ch == u[j]:
                    new_dp[i][j+1] = True
        dp = new_dp

    return dp[lt][lu]

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    s = lines[0]
    patterns = lines[1:]
    n = len(patterns)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                # Can the same string be embedded twice as disjoint subsequences?
                result = can_interleave(s, patterns[i], patterns[j])
            else:
                result = can_interleave(s, patterns[i], patterns[j])
            row.append('1' if result else '0')
        matrix.append(' '.join(row))
    print('\n'.join(matrix))

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
