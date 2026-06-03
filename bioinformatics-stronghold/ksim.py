# Finding All Similar Motifs (KSIM)
# Rosalind problem: https://rosalind.info/problems/ksim/
#
# Problem: Given a long string s, a shorter pattern t, and a threshold k,
# find every substring of s whose fitting alignment score with t is ≥ k.
# Scoring: match +1, mismatch −1, gap −1.
#
# Algorithm: Same fitting-alignment DP as SIMS, but we record every column j
# in the last row where dp[len(t)][j] >= k.  For each such j, trace back to
# recover the aligned substring of s.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_ksim.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    records, current_id, parts = [], None, []
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

GAP = -1

def sc(a, b):
    return 1 if a == b else -1

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    # First non-FASTA line that starts with a digit is k; otherwise first line is k
    if lines[0].lstrip('-').isdigit():
        k = int(lines[0])
        rest = '\n'.join(lines[1:])
    else:
        k = int(lines[-1])
        rest = '\n'.join(lines[:-1])

    seqs = parse_fasta(rest)
    if len(seqs) >= 2:
        s, t = seqs[0], seqs[1]
    else:
        s, t = lines[1], lines[2]

    m, n = len(s), len(t)

    NEG_INF = float('-inf')
    dp   = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    back = [[None]    * (m + 1) for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = 0
    for i in range(1, n + 1):
        dp[i][0] = GAP * i
        back[i][0] = 'up'

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i-1][j-1] + sc(t[i-1], s[j-1])
            up   = dp[i-1][j]   + GAP
            left = dp[i][j-1]   + GAP
            best = max(diag, up, left)
            dp[i][j] = best
            back[i][j] = 'diag' if best == diag else ('up' if best == up else 'left')

    def traceback(end_j):
        i, j = n, end_j
        aln_s = []
        while i > 0:
            d = back[i][j]
            if d == 'diag':
                aln_s.append(s[j-1]); i -= 1; j -= 1
            elif d == 'up':
                aln_s.append('-'); i -= 1
            else:
                aln_s.append(s[j-1]); j -= 1
        aln_s.reverse()
        return j, ''.join(aln_s)

    results = []
    for j in range(1, m + 1):
        if dp[n][j] >= k:
            start_j, aln_s = traceback(j)
            results.append((start_j + 1, j, dp[n][j], aln_s))  # 1-based

    for start, end, score_val, aln in sorted(results):
        print(f'{score_val}')
        print(aln)

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
