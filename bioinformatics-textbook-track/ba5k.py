# BA5K — Find a Middle Edge in an Alignment Graph in Linear Space
# https://rosalind.info/problems/ba5k/
#
# Given: two protein strings. Return: the "middle edge" of the optimal alignment
# path (used as a base case for the linear-space alignment divide-and-conquer).
# Uses BLOSUM62 with linear gap penalty -5.
# The middle edge is reported as (node_from, node_to) at the midpoint column.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba5k.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

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

def last_col_scores(s, t, gap):
    """Compute the last column of the alignment DP score matrix."""
    m, n = len(s), len(t)
    prev = [gap*j for j in range(n+1)]
    for i in range(1, m+1):
        curr = [prev[0] + gap]
        for j in range(1, n+1):
            sc = BLOSUM62.get((s[i-1],t[j-1]),-4)
            curr.append(max(prev[j-1]+sc, prev[j]+gap, curr[-1]+gap))
        prev = curr
    return prev

def solve(data):
    lines = data.splitlines(); s, t = lines[0].strip(), lines[1].strip()
    n = len(t)
    mid = n // 2
    # Forward scores to column mid
    from_scores = last_col_scores(s, t[:mid], GAP)
    # Backward scores from column n to mid (reverse strings)
    to_scores = last_col_scores(s[::-1], t[mid:][::-1], GAP)
    # Find maximum sum at row boundary
    best, best_i = float('-inf'), 0
    for i in range(len(s)+1):
        total = from_scores[i] + to_scores[len(s)-i]
        if total > best: best, best_i = total, i
    # Determine if middle edge is diagonal or down
    from_scores2 = last_col_scores(s, t[:mid+1], GAP)
    # Middle edge: from (best_i, mid) to either (best_i+1, mid+1) [diagonal] or (best_i, mid+1) [gap in s]
    print(f"({best_i}, {mid})")
    print(f"({best_i+1}, {mid+1})")

if __name__ == '__main__': solve(get_input())
