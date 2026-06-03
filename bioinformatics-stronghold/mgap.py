# Maximizing the Gap Symbols of an Optimal Alignment (MGAP)
# Rosalind problem: https://rosalind.info/problems/mgap/
#
# Problem: Given two protein strings (in FASTA), find the maximum number of
# gap symbols that appear in any optimal global alignment using BLOSUM62
# with a linear gap penalty of -1.
#
# Algorithm: Two coupled DPs.
#   dp_score[i][j] = maximum global alignment score for s[0..i-1] vs t[0..j-1].
#   dp_gaps[i][j]  = maximum gap count among all alignments achieving dp_score[i][j].
# For dp_gaps, whenever multiple predecessors achieve the same score, take the
# one that maximises gap count.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_mgap.txt')
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
        for j, sc in enumerate(parts[1:]):
            mat[(aa, aas[j])] = int(sc)
    return mat

BLOSUM62 = _build_blosum62()
GAP = -1

def solve(data):
    seqs = parse_fasta(data)
    s, t = seqs[0], seqs[1]
    m, n = len(s), len(t)

    NEG_INF = float('-inf')
    dp_score = [[NEG_INF] * (n + 1) for _ in range(m + 1)]
    dp_gaps  = [[0]       * (n + 1) for _ in range(m + 1)]

    dp_score[0][0] = 0
    for i in range(1, m + 1):
        dp_score[i][0] = GAP * i
        dp_gaps[i][0]  = i
    for j in range(1, n + 1):
        dp_score[0][j] = GAP * j
        dp_gaps[0][j]  = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sc = BLOSUM62.get((s[i-1], t[j-1]), -4)
            candidates = [
                (dp_score[i-1][j-1] + sc,      dp_gaps[i-1][j-1]),      # match/mismatch
                (dp_score[i-1][j]   + GAP,      dp_gaps[i-1][j]   + 1),  # gap in t
                (dp_score[i][j-1]   + GAP,      dp_gaps[i][j-1]   + 1),  # gap in s
            ]
            best_sc = max(c[0] for c in candidates)
            best_g  = max(c[1] for c in candidates if c[0] == best_sc)
            dp_score[i][j] = best_sc
            dp_gaps[i][j]  = best_g

    print(dp_gaps[m][n])

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
