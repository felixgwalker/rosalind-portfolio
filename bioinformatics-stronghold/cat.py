# Catalan Numbers and RNA Secondary Structures (CAT)
# Rosalind problem: https://rosalind.info/problems/cat/
#
# Problem: Given an RNA string s of even length, with equal numbers of A and U
# (and equal numbers of G and C), return the number of noncrossing perfect
# matchings of its base-pair edges modulo 1,000,000.
#
# Algorithm: Interval DP.
#   dp[i][j] = number of noncrossing perfect matchings for substring s[i..j].
#   Base: dp[i][i] = 0 (can't pair single base), dp[i][i-1] = 1 (empty = 1 way).
#   Recurrence: s[i] must be paired with some s[k] where k > i and k-i is odd
#   (so the segment between them is even-length). For each valid pairing s[i]-s[k]:
#     dp[i][j] += dp[i+1][k-1] * dp[k+1][j]
#   Valid pairs: A-U, U-A, G-C, C-G.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_cat.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read(), None

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

    # dp[i][j] = noncrossing perfect matchings of s[i..j]
    dp = [[0] * n for _ in range(n)]

    # Fill by increasing interval length
    for length in range(2, n + 1, 2):   # only even lengths can have perfect matchings
        for i in range(n - length + 1):
            j = i + length - 1
            # s[i] must pair with some s[k] where k is in {i+1, i+3, ..., j}
            # (k-i must be odd so both sub-intervals are even-length)
            for k in range(i + 1, j + 1, 2):
                if (s[i], s[k]) in PAIRS:
                    # Sub-interval i+1..k-1 (length k-i-1, even) and k+1..j
                    left = dp[i+1][k-1] if k > i + 1 else 1   # empty interval = 1
                    right = dp[k+1][j] if k < j else 1
                    dp[i][j] = (dp[i][j] + left * right) % MOD

    print(dp[0][n-1])

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
