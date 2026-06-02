# Suboptimal Local Alignment (SUBO)
# Rosalind problem: https://rosalind.info/problems/subo/
#
# Problem: Given two DNA strings s and t in FASTA format, return the number of
# optimal and suboptimal local alignments of s and t with score equal to the
# maximum Smith-Waterman score.
#
# Scoring: match +3, mismatch -1, gap opening -5, gap extension -1.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_subo.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

MATCH    =  3
MISMATCH = -1
GAP_OPEN = -5
GAP_EXT  = -1

def parse_fasta(text):
    records, cur_id, parts = [], None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if cur_id is not None:
                records.append(''.join(parts))
            cur_id, parts = line[1:], []
        else:
            parts.append(line)
    if cur_id is not None:
        records.append(''.join(parts))
    return records

def sw_affine(s, t):
    """Smith-Waterman with affine gap penalties.
    Returns the best score and the full score matrix."""
    m, n = len(s), len(t)
    NEG = float('-inf')
    H = [[0.0] * (n + 1) for _ in range(m + 1)]   # main SW matrix
    E = [[NEG]  * (n + 1) for _ in range(m + 1)]   # gap in t (horizontal)
    F = [[NEG]  * (n + 1) for _ in range(m + 1)]   # gap in s (vertical)

    best = 0.0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sub = MATCH if s[i-1] == t[j-1] else MISMATCH
            E[i][j] = max(H[i][j-1] + GAP_OPEN + GAP_EXT, E[i][j-1] + GAP_EXT)
            F[i][j] = max(H[i-1][j] + GAP_OPEN + GAP_EXT, F[i-1][j] + GAP_EXT)
            H[i][j] = max(0, H[i-1][j-1] + sub, E[i][j], F[i][j])
            if H[i][j] > best:
                best = H[i][j]
    return best, H

def solve(data):
    seqs = parse_fasta(data)
    if len(seqs) < 2:
        return
    s, t = seqs[0].upper(), seqs[1].upper()
    best, H = sw_affine(s, t)
    count = sum(1 for row in H for v in row if v == best)
    print(int(best))
    print(count)

if __name__ == '__main__':
    solve(get_input())
