# Wobble Bonding and RNA Secondary Structures (RNAS)
# Rosalind problem: https://rosalind.info/problems/rnas/
#
# Problem: Given an RNA string s (in FASTA), count all valid noncrossing
# matchings of basepair edges (partial matchings allowed, including the
# trivial matching with no edges), where pairs may be standard Watson-Crick
# pairs (A-U, U-A, G-C, C-G) or wobble pairs (G-U, U-G), subject to the
# constraint that a basepair edge connecting s[i] and s[k] requires
# k - i >= 4 (minimum hairpin loop size of 3 unpaired bases).
# Return the exact count (no modulus — answers fit in Python's big ints).
#
# This is MOTZ's interval DP extended with wobble pairs and the minimum
# loop-length constraint. O(n³).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_rnas.txt')
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

# Standard pairs + wobble G-U pairs
PAIRS = {('A','U'), ('U','A'), ('G','C'), ('C','G'), ('G','U'), ('U','G')}
MIN_GAP = 4   # a basepair edge between s[i] and s[k] requires k - i >= 4

def solve(data):
    s = parse_fasta(data)
    n = len(s)

    # dp[i][j] = number of valid noncrossing matchings of s[i..j]
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1   # single base: only the trivial (empty) matching

    def get(i, j):
        if i > j:
            return 1   # empty interval: one way (no edges)
        return dp[i][j]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            val = get(i + 1, j)   # s[i] unmatched
            for k in range(i + MIN_GAP, j + 1):
                if (s[i], s[k]) in PAIRS:
                    val += get(i + 1, k - 1) * get(k + 1, j)
            dp[i][j] = val

    print(get(0, n - 1))

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
