# Pairwise Global Alignment (MULT)
# Rosalind problem: https://rosalind.info/problems/mult/
#
# Problem: Given 2–4 protein sequences in FASTA, perform pairwise global
# alignments using BLOSUM62 with gap-open=-10, gap-extend=-1 and return the
# score of the highest-scoring pairwise alignment.
#
# Implements Needleman-Wunsch with affine gap penalties.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_mult.txt')
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
                records.append((current_id, ''.join(parts)))
            current_id, parts = line[1:], []
        else:
            parts.append(line)
    if current_id is not None:
        records.append((current_id, ''.join(parts)))
    return records

BLOSUM62_STR = """   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
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
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4"""

def build_blosum62():
    lines = [l for l in BLOSUM62_STR.strip().splitlines() if l.strip()]
    aas = lines[0].split()
    mat = {}
    for row in lines[1:]:
        parts = row.split()
        aa = parts[0]
        for j, sc in enumerate(parts[1:]):
            mat[(aa, aas[j])] = int(sc)
    return mat

BLOSUM62 = build_blosum62()
GAP_OPEN = -10
GAP_EXT = -1
NEG_INF = float('-inf')

def affine_global_score(s, t):
    """Needleman-Wunsch with affine gaps. Returns score only."""
    m, n = len(s), len(t)
    M = [[NEG_INF] * (n+1) for _ in range(m+1)]
    X = [[NEG_INF] * (n+1) for _ in range(m+1)]
    Y = [[NEG_INF] * (n+1) for _ in range(m+1)]
    M[0][0] = 0
    for i in range(1, m+1):
        X[i][0] = GAP_OPEN + (i-1) * GAP_EXT
    for j in range(1, n+1):
        Y[0][j] = GAP_OPEN + (j-1) * GAP_EXT
    for i in range(1, m+1):
        for j in range(1, n+1):
            sc = BLOSUM62.get((s[i-1], t[j-1]), -4)
            M[i][j] = sc + max(M[i-1][j-1], X[i-1][j-1], Y[i-1][j-1])
            X[i][j] = max(M[i-1][j] + GAP_OPEN, X[i-1][j] + GAP_EXT)
            Y[i][j] = max(M[i][j-1] + GAP_OPEN, Y[i][j-1] + GAP_EXT)
    return max(M[m][n], X[m][n], Y[m][n])

def solve(data):
    records = parse_fasta(data)
    seqs = [seq for _, seq in records]
    if len(seqs) < 2:
        print(0)
        return
    # Find highest-scoring pairwise alignment
    best = NEG_INF
    for i in range(len(seqs)):
        for j in range(i+1, len(seqs)):
            sc = affine_global_score(seqs[i], seqs[j])
            if sc > best:
                best = sc
    print(best)

if __name__ == '__main__':
    solve(get_input())
