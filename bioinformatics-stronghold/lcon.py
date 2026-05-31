# Local Alignment with Constant Gap Penalty (LCON)
# Rosalind problem: https://rosalind.info/problems/lcon/
#
# Problem: Local alignment of two protein strings with BLOSUM62 and a constant
# gap penalty of -5 per gap block (regardless of gap length).
#
# Algorithm: 3-matrix Smith-Waterman with constant gap penalty.
#   All three matrices have a floor of 0 (local alignment restarts on negative scores).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_lcon.txt')
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

# Reuse BLOSUM62 definition (inline to keep file self-contained)
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
def _build():
    lines = [l for l in BLOSUM62_STR.strip().splitlines() if l.strip()]
    aas = lines[0].split()
    mat = {}
    for row in lines[1:]:
        parts = row.split()
        aa = parts[0]
        for j, sc in enumerate(parts[1:]):
            mat[(aa, aas[j])] = int(sc)
    return mat

BLOSUM62 = _build()
GAP_CONST = -5
NEG_INF = float('-inf')

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    m, n = len(s), len(t)

    M = [[0]*(n+1) for _ in range(m+1)]
    X = [[NEG_INF]*(n+1) for _ in range(m+1)]
    Y = [[NEG_INF]*(n+1) for _ in range(m+1)]

    best = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            sc = BLOSUM62.get((s[i-1], t[j-1]), -4)
            M[i][j] = max(0, M[i-1][j-1]+sc, X[i-1][j-1]+sc, Y[i-1][j-1]+sc)
            X[i][j] = max(0, X[i-1][j], M[i-1][j]+GAP_CONST, Y[i-1][j]+GAP_CONST)
            Y[i][j] = max(0, Y[i][j-1], M[i][j-1]+GAP_CONST, X[i][j-1]+GAP_CONST)
            best = max(best, M[i][j], X[i][j], Y[i][j])

    print(best)

if __name__ == '__main__':
    solve(get_input())
