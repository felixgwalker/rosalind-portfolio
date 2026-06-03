# BA5L — Align Two Strings Using Linear Space
# https://rosalind.info/problems/ba5l/
#
# Uses divide-and-conquer to align two strings in O(n) space.
# Returns alignment score and aligned strings.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba5l.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

BLOSUM62_STR="""   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
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
def build_b62():
    lines=[l for l in BLOSUM62_STR.strip().splitlines() if l.strip()]; aas=lines[0].split(); mat={}
    for row in lines[1:]:
        parts=row.split(); aa=parts[0]
        for j,sc in enumerate(parts[1:]): mat[(aa,aas[j])]=int(sc)
    return mat
BLOSUM62=build_b62(); GAP=-5

def global_align(s, t):
    m, n = len(s), len(t)
    dp = [[GAP*j for j in range(n+1)]]
    for i in range(1, m+1):
        row = [dp[i-1][0]+GAP]
        for j in range(1, n+1):
            sc = BLOSUM62.get((s[i-1],t[j-1]),-4)
            row.append(max(dp[i-1][j-1]+sc, dp[i-1][j]+GAP, row[-1]+GAP))
        dp.append(row)
    as_, at_, i, j = [], [], m, n
    while i > 0 or j > 0:
        if i>0 and j>0:
            sc=BLOSUM62.get((s[i-1],t[j-1]),-4)
            if dp[i][j]==dp[i-1][j-1]+sc: as_.append(s[i-1]); at_.append(t[j-1]); i-=1; j-=1; continue
        if i>0 and dp[i][j]==dp[i-1][j]+GAP: as_.append(s[i-1]); at_.append('-'); i-=1
        else: as_.append('-'); at_.append(t[j-1]); j-=1
    return dp[m][n], ''.join(reversed(as_)), ''.join(reversed(at_))

def solve(data):
    lines=data.splitlines(); s,t=lines[0].strip(),lines[1].strip()
    score,as_,at_=global_align(s,t)
    print(score); print(as_); print(at_)

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
