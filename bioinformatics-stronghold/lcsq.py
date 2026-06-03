# Finding a Shared Spliced Motif (LCSQ)
# Rosalind problem: https://rosalind.info/problems/lcsq/
#
# Problem: Given two DNA strings s and t (in FASTA format, each ≤ 1000 nt),
# find the longest common subsequence — the longest string that is a
# subsequence of both s and t.
#
# Algorithm: Standard LCS dynamic programming.
#   dp[i][j] = length of LCS of s[0..i-1] and t[0..j-1].
#   dp[i][j] = dp[i-1][j-1] + 1       if s[i-1] == t[j-1]
#            = max(dp[i-1][j], dp[i][j-1])  otherwise
#   Backtrack through the dp table to recover one LCS string.
#   O(|s|·|t|) time and space.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_lcsq.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    records = []
    current_id, parts = None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if current_id is not None:
                records.append(''.join(parts))
            current_id, parts = line[1:], []
        else:
            parts.append(line)
    if current_id is not None:
        records.append(''.join(parts))
    return records

def lcs(s, t):
    m, n = len(s), len(t)
    # Build DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to recover one LCS
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            result.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(result))

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    print(lcs(s, t))

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
