# Edit Distance Alignment (EDTA)
# Rosalind problem: https://rosalind.info/problems/edta/
#
# Problem: Given two protein strings s and t (in FASTA format), compute the edit
# distance and output the alignment that achieves it. Uses the same DP as EDIT
# but also backtracks to recover the aligned strings.
#
# Alignment notation: gaps are represented by '-'.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_edta.txt')
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

def edit_alignment(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    # Backtrack
    aligned_s, aligned_t = [], []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s[i-1] == t[j-1] and dp[i][j] == dp[i-1][j-1]:
            aligned_s.append(s[i-1])
            aligned_t.append(t[j-1])
            i -= 1; j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            aligned_s.append(s[i-1])
            aligned_t.append(t[j-1])
            i -= 1; j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            aligned_s.append(s[i-1])
            aligned_t.append('-')
            i -= 1
        else:
            aligned_s.append('-')
            aligned_t.append(t[j-1])
            j -= 1

    return dp[m][n], ''.join(reversed(aligned_s)), ''.join(reversed(aligned_t))

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    dist, as_, at_ = edit_alignment(s, t)
    print(dist)
    print(as_)
    print(at_)

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
