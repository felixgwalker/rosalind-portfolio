# Global Alignment with Scoring Matrix (GLOB)
# Rosalind problem: https://rosalind.info/problems/glob/
#
# Problem: Given two protein strings s and t (≤ 1000 aa each), compute the
# maximum score of a global alignment using the BLOSUM62 substitution matrix
# and a linear gap penalty of -5 per gap character.
#
# Algorithm: Needleman-Wunsch DP.
#   dp[i][j] = best score aligning s[0..i-1] with t[0..j-1].
#   dp[i][j] = max(dp[i-1][j-1] + BLOSUM62[s[i-1]][t[j-1]],
#                  dp[i-1][j]   - 5,     # gap in t (delete from s)
#                  dp[i][j-1]   - 5)     # gap in s (insert into s)

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_glob.txt')
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

# BLOSUM62 matrix (from NCBI)
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
GAP = -5

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    m, n = len(s), len(t)

    # Needleman-Wunsch DP (full table for alignment score only)
    INF = float('-inf')
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for i in range(1, m + 1):
        dp[i][0] = GAP * i
    for j in range(1, n + 1):
        dp[0][j] = GAP * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dp[i-1][j-1] + BLOSUM62.get((s[i-1], t[j-1]), -4)
            delete = dp[i-1][j] + GAP
            insert = dp[i][j-1] + GAP
            dp[i][j] = max(match, delete, insert)

    print(dp[m][n])

if __name__ == '__main__':
    solve(get_input())
