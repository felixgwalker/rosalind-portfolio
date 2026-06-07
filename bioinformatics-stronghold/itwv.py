# Finding Disjoint Motifs in a Gene (ITWV)
# Rosalind problem: https://rosalind.info/problems/itwv/
#
# Problem: Given a string s and a collection of patterns, output a matrix where
# entry (i, j) is 1 iff there is SOME SUBSTRING of s that is an interleaving
# (shuffle) of pattern i and pattern j as disjoint subsequences -- i.e. a
# contiguous window of s of length len(t) + len(u) whose characters can be
# partitioned, in order, into t and u using every character of the window.
#
# Algorithm: for each window w of s of length len(t) + len(u), run the classic
# "interleaving string" DP:
#   dp[i][j] = True iff w[:i+j] is an interleaving of t[:i] and u[:j]
#   dp[i][j] = (dp[i-1][j] and t[i-1] == w[i+j-1]) or
#              (dp[i][j-1] and u[j-1] == w[i+j-1])
# The pair matches if dp[len(t)][len(u)] is True for any window.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_itwv.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def is_interleaving(w, t, u):
    """Check if w (with len(w) == len(t) + len(u)) is an interleaving of t and u."""
    lt, lu = len(t), len(u)
    dp = [[False] * (lu + 1) for _ in range(lt + 1)]
    dp[0][0] = True
    for i in range(lt + 1):
        for j in range(lu + 1):
            if i == 0 and j == 0:
                continue
            dp[i][j] = (
                (i > 0 and dp[i-1][j] and t[i-1] == w[i+j-1]) or
                (j > 0 and dp[i][j-1] and u[j-1] == w[i+j-1])
            )
    return dp[lt][lu]

def can_interleave(s, t, u):
    """Check if some substring of s is an interleaving of t and u as disjoint subsequences."""
    window = len(t) + len(u)
    return any(is_interleaving(s[k:k+window], t, u)
               for k in range(len(s) - window + 1))

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    s = lines[0]
    patterns = lines[1:]
    n = len(patterns)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
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
