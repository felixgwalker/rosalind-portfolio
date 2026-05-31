# Global Alignment with Scoring Matrix and Affine Gap Penalty (GAFF)
# Rosalind problem: https://rosalind.info/problems/gaff/
#
# Problem: Global alignment of two protein strings using BLOSUM62 with affine
# gap penalties: gap open = -11, gap extend = -1.
#   Gap of length k costs: -11 - (k-1)*1 = -(k+10) = -11 for k=1, -12 for k=2, etc.
#
# Algorithm: 3-matrix Needleman-Wunsch.
#   M[i][j]  = best score ending with s[i-1] aligned to t[j-1] (match/mismatch)
#   X[i][j]  = best score ending with a gap in t (deletion in t, s[i-1] aligned to -)
#   Y[i][j]  = best score ending with a gap in s (insertion into s, - aligned to t[j-1])

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_gaff.txt')
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

BLOSUM62_STR = """
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""

def _build_blosum62():
    lines = [l for l in BLOSUM62_STR.strip().splitlines() if l.strip()]
    aas = lines[0].split()
    mat = {}
    for row in lines[1:]:
        parts = row.split()
        aa = parts[0]
        for j, score in enumerate(parts[1:]):
            mat[(aa, aas[j])] = int(score)
    return mat

BLOSUM62 = _build_blosum62()
GAP_OPEN = -11    # penalty when a gap starts
GAP_EXT = -1      # penalty per extension (additional character)
NEG_INF = float('-inf')

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    m, n = len(s), len(t)

    # Three score matrices
    M = [[NEG_INF] * (n + 1) for _ in range(m + 1)]
    X = [[NEG_INF] * (n + 1) for _ in range(m + 1)]   # gap in t
    Y = [[NEG_INF] * (n + 1) for _ in range(m + 1)]   # gap in s

    M[0][0] = 0
    for i in range(1, m + 1):
        X[i][0] = GAP_OPEN + (i - 1) * GAP_EXT
    for j in range(1, n + 1):
        Y[0][j] = GAP_OPEN + (j - 1) * GAP_EXT

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score = BLOSUM62.get((s[i-1], t[j-1]), -4)
            M[i][j] = score + max(M[i-1][j-1], X[i-1][j-1], Y[i-1][j-1])
            X[i][j] = max(M[i-1][j] + GAP_OPEN,
                          X[i-1][j] + GAP_EXT)
            Y[i][j] = max(M[i][j-1] + GAP_OPEN,
                          Y[i][j-1] + GAP_EXT)

    best = max(M[m][n], X[m][n], Y[m][n])
    print(best)

if __name__ == '__main__':
    solve(get_input())
