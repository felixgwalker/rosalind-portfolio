# Local Alignment with Scoring Matrix (LOCA)
# Rosalind problem: https://rosalind.info/problems/loca/
#
# Problem: Given two protein strings s and t (≤ 1000 aa each) in FASTA format,
# find the highest-scoring local alignment using the PAM250 substitution matrix
# with a linear gap penalty of -5.
#
# Algorithm: Smith-Waterman DP.
#   dp[i][j] = best local alignment score ending at s[i-1], t[j-1]
#   dp[i][j] = max(0,
#                  dp[i-1][j-1] + PAM250[s[i-1]][t[j-1]],
#                  dp[i-1][j]   - 5,
#                  dp[i][j-1]   - 5)
#   Output: score, then the two aligned substrings achieving it.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_loca.txt')
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

# PAM250 matrix (a commonly used local alignment matrix)
PAM250_STR = """
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
"""

def _build_pam250():
    lines = [l for l in PAM250_STR.strip().splitlines() if l.strip()]
    aas = lines[0].split()
    mat = {}
    for row in lines[1:]:
        parts = row.split()
        aa = parts[0]
        for j, score in enumerate(parts[1:]):
            mat[(aa, aas[j])] = int(score)
    return mat

PAM250 = _build_pam250()
GAP = -5

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    m, n = len(s), len(t)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best_score = 0
    best_pos = (0, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score = PAM250.get((s[i-1], t[j-1]), -5)
            dp[i][j] = max(0,
                           dp[i-1][j-1] + score,
                           dp[i-1][j] + GAP,
                           dp[i][j-1] + GAP)
            if dp[i][j] > best_score:
                best_score = dp[i][j]
                best_pos = (i, j)

    # Backtrack
    aligned_s, aligned_t = [], []
    i, j = best_pos
    while i > 0 and j > 0 and dp[i][j] > 0:
        score = PAM250.get((s[i-1], t[j-1]), -5)
        if dp[i][j] == dp[i-1][j-1] + score:
            aligned_s.append(s[i-1])
            aligned_t.append(t[j-1])
            i -= 1; j -= 1
        elif dp[i][j] == dp[i-1][j] + GAP:
            aligned_s.append(s[i-1])
            aligned_t.append('-')
            i -= 1
        else:
            aligned_s.append('-')
            aligned_t.append(t[j-1])
            j -= 1

    print(best_score)
    print(''.join(reversed(aligned_s)))
    print(''.join(reversed(aligned_t)))

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
