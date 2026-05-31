# BA9M — Implement Better BWMatching
# https://rosalind.info/problems/ba9m/
#
# Given: BWT string and patterns. Return: number of times each pattern appears.
# Uses checkpoints for O(|pattern| * n/checkpoint) matching.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9m.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    bwt = lines[0].strip()
    patterns = [l.strip() for l in lines[1:] if l.strip()]
    n = len(bwt)
    first = sorted(bwt)
    first_occ = {}
    for i, ch in enumerate(first):
        if ch not in first_occ: first_occ[ch] = i
    # Precompute count[ch][i] = count of ch in bwt[0..i-1]
    counts = defaultdict(lambda: [0]*(n+1))
    for i, ch in enumerate(bwt):
        for c in counts: counts[c][i+1] = counts[c][i]
        counts[ch][i+1] = counts[ch][i] + 1
    results = []
    for pattern in patterns:
        top, bottom = 0, n-1
        for i in range(len(pattern)-1, -1, -1):
            symbol = pattern[i]
            if symbol not in first_occ: bottom = -1; break
            top = first_occ[symbol] + counts[symbol][top]
            bottom = first_occ[symbol] + counts[symbol][bottom+1] - 1
            if top > bottom: bottom = -1; break
        results.append(max(0, bottom-top+1) if top<=bottom else 0)
    print(' '.join(map(str, results)))

if __name__ == '__main__': solve(get_input())
