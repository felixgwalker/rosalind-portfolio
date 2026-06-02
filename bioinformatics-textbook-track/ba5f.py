# BA5F — Find a Highest-Scoring Local Alignment
# https://rosalind.info/problems/ba5f/
#
# Given: two protein strings.
# Return: the score and a local alignment using PAM250, linear gap penalty -5.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba5f.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

PAM250_STR="""   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
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
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10"""

def build_pam250():
    lines = [l for l in PAM250_STR.strip().splitlines() if l.strip()]
    aas = lines[0].split(); mat = {}
    for row in lines[1:]:
        parts = row.split(); aa = parts[0]
        for j, sc in enumerate(parts[1:]): mat[(aa, aas[j])] = int(sc)
    return mat

PAM250 = build_pam250()
GAP = -5

def local_align(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    best, best_pos = 0, (0, 0)
    for i in range(1, m+1):
        for j in range(1, n+1):
            sc = PAM250.get((s[i-1],t[j-1]),-5)
            dp[i][j] = max(0, dp[i-1][j-1]+sc, dp[i-1][j]+GAP, dp[i][j-1]+GAP)
            if dp[i][j] > best: best, best_pos = dp[i][j], (i,j)
    as_, at_, i, j = [], [], *best_pos
    while i > 0 and j > 0 and dp[i][j] > 0:
        sc = PAM250.get((s[i-1],t[j-1]),-5)
        if dp[i][j] == dp[i-1][j-1]+sc: as_.append(s[i-1]); at_.append(t[j-1]); i-=1; j-=1
        elif dp[i][j] == dp[i-1][j]+GAP: as_.append(s[i-1]); at_.append('-'); i-=1
        else: as_.append('-'); at_.append(t[j-1]); j-=1
    return best, ''.join(reversed(as_)), ''.join(reversed(at_))

def solve(data):
    lines = data.splitlines(); s, t = lines[0].strip(), lines[1].strip()
    score, as_, at_ = local_align(s, t)
    print(score); print(as_); print(at_)

if __name__ == '__main__': solve(get_input())
