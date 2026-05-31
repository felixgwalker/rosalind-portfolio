# BA9L — Implement BWMatching
# https://rosalind.info/problems/ba9l/
#
# Given: BWT string and a collection of patterns.
# Return: the number of times each pattern appears in the original string.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9l.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def bw_matching(bwt, patterns):
    n = len(bwt)
    first = sorted(bwt)
    # First column occurrences
    first_occ = {}
    for i, ch in enumerate(first):
        if ch not in first_occ: first_occ[ch] = i
    # Count array for BWT
    results = []
    for pattern in patterns:
        top, bottom = 0, n-1
        i = len(pattern)-1
        while top <= bottom:
            if i < 0: break
            symbol = pattern[i]; i -= 1
            # Count symbol in bwt[top..bottom]
            top_count = sum(1 for j in range(top) if bwt[j]==symbol)
            bottom_count = sum(1 for j in range(bottom+1) if bwt[j]==symbol)
            if bottom_count <= top_count: bottom = -1; break
            top = first_occ.get(symbol, n) + top_count
            bottom = first_occ.get(symbol, n) + bottom_count - 1
        results.append(max(0, bottom - top + 1) if top <= bottom else 0)
    return results

def solve(data):
    lines = data.splitlines()
    bwt = lines[0].strip()
    patterns = [l.strip() for l in lines[1:] if l.strip()]
    counts = bw_matching(bwt, patterns)
    print(' '.join(map(str, counts)))

if __name__ == '__main__': solve(get_input())
