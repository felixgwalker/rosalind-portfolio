# Edit Distance (EDIT)
# Rosalind problem: https://rosalind.info/problems/edit/
#
# Problem: Given two protein strings s and t (in FASTA format, each ≤ 1000 aa),
# compute the edit distance (Levenshtein distance) — the minimum number of
# single-character insertions, deletions, and substitutions needed to transform s into t.
#
# Algorithm: Standard DP.
#   dp[i][j] = edit distance between s[0..i-1] and t[0..j-1]
#   dp[i][j] = dp[i-1][j-1]           if s[i-1] == t[j-1]  (no change needed)
#            = 1 + min(dp[i-1][j-1],  # substitution
#                      dp[i-1][j],    # deletion from s
#                      dp[i][j-1])    # insertion into s
#   O(|s|·|t|) time and space.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_edit.txt')
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

def edit_distance(s, t):
    m, n = len(s), len(t)
    # Space-optimised: keep only two rows
    prev = list(range(n + 1))   # dp[i-1][0..n]
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j-1], prev[j], curr[j-1])
        prev = curr
    return prev[n]

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    print(edit_distance(s, t))

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
