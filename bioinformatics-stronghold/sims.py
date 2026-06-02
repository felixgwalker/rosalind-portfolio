# Finding a Motif with Modifications (SIMS)
# Rosalind problem: https://rosalind.info/problems/sims/
#
# Problem: Given a long string s and a shorter pattern t (both as plain strings
# or the first two FASTA records), find the substring of s that most closely
# matches t — i.e., the highest-scoring "fitting alignment" of t inside s.
# Scoring: match +1, mismatch −1, gap −1.
#
# Algorithm: Fitting alignment DP.
#   Rows = positions in t (0..len(t)), columns = positions in s (0..len(s)).
#   dp[0][j] = 0 for all j  (pattern can start anywhere in s, free leading skip)
#   dp[i][0] = -i            (all of t[0..i-1] gapped costs -i)
#   Answer   = max over dp[len(t)][j] for all j.
#   Traceback from the maximising column back to row 0; read the s-column range.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_sims.txt')
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

def score(a, b):
    return 1 if a == b else -1

def solve(data):
    seqs = parse_fasta(data)
    if len(seqs) >= 2:
        s, t = seqs[0], seqs[1]
    else:
        lines = [l.strip() for l in data.splitlines() if l.strip()]
        s, t = lines[0], lines[1]

    m, n = len(s), len(t)  # s = text, t = pattern

    NEG_INF = float('-inf')
    # dp[i][j]: best fitting-alignment score for t[0..i-1] against a substr of s ending at j
    dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = 0
    for i in range(1, n + 1):
        dp[i][0] = GAP * i
        back[i][0] = 'up'

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i-1][j-1] + score(t[i-1], s[j-1])
            up   = dp[i-1][j]   + GAP
            left = dp[i][j-1]   + GAP
            best = max(diag, up, left)
            dp[i][j] = best
            if best == diag:
                back[i][j] = 'diag'
            elif best == up:
                back[i][j] = 'up'
            else:
                back[i][j] = 'left'

    # Find best ending column
    best_score = max(dp[n][j] for j in range(m + 1))
    end_j = next(j for j in range(m, -1, -1) if dp[n][j] == best_score)

    # Traceback to find alignment and the starting column in s
    i, j = n, end_j
    aln_t, aln_s = [], []
    while i > 0:
        d = back[i][j]
        if d == 'diag':
            aln_t.append(t[i-1]); aln_s.append(s[j-1]); i -= 1; j -= 1
        elif d == 'up':
            aln_t.append(t[i-1]); aln_s.append('-'); i -= 1
        else:
            aln_t.append('-'); aln_s.append(s[j-1]); j -= 1

    aln_t.reverse(); aln_s.reverse()
    start_j = j  # column in s where alignment starts (0-based)

    print(best_score)
    print(''.join(aln_s))
    print(''.join(aln_t))

if __name__ == '__main__':
    solve(get_input())
