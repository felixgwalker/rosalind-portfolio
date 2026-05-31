# Global Alignment with Constant Gap Penalty (GCON)
# Rosalind problem: https://rosalind.info/problems/gcon/
#
# Problem: Global alignment of two protein strings with BLOSUM62 and a constant
# gap penalty: every gap block (any length ≥ 1) is penalised by a fixed -5,
# regardless of its length. This contrasts with linear (-5 per character) or
# affine penalties.
#
# Algorithm: 3-matrix DP similar to affine but with different recurrences.
#   M[i][j]  = best score ending with a match/mismatch
#   X[i][j]  = best score ending with a gap in t (from the s side)
#   Y[i][j]  = best score ending with a gap in s (from the t side)
#   Opening a gap costs -5; extending it costs 0.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_gcon.txt')
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
GAP_CONST = -5   # constant gap penalty (any-length gap costs this much)
NEG_INF = float('-inf')

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    m, n = len(s), len(t)

    M = [[NEG_INF]*(n+1) for _ in range(m+1)]
    X = [[NEG_INF]*(n+1) for _ in range(m+1)]
    Y = [[NEG_INF]*(n+1) for _ in range(m+1)]
    M[0][0] = 0
    for i in range(1, m+1):
        X[i][0] = GAP_CONST
    for j in range(1, n+1):
        Y[0][j] = GAP_CONST

    for i in range(1, m+1):
        for j in range(1, n+1):
            sc = BLOSUM62.get((s[i-1], t[j-1]), -4)
            M[i][j] = sc + max(M[i-1][j-1], X[i-1][j-1], Y[i-1][j-1])
            # Extend gap (free) or open new gap from M or Y
            X[i][j] = max(X[i-1][j],               # extend existing gap in t
                          M[i-1][j] + GAP_CONST,    # open new gap in t from match
                          Y[i-1][j] + GAP_CONST)    # open new gap in t from gap in s
            Y[i][j] = max(Y[i][j-1],
                          M[i][j-1] + GAP_CONST,
                          X[i][j-1] + GAP_CONST)

    print(max(M[m][n], X[m][n], Y[m][n]))

if __name__ == '__main__':
    solve(get_input())
