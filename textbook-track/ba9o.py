# BA9O — Find All Occurrences of a Collection of Patterns in a String Using BWT (Advanced)
# https://rosalind.info/problems/ba9o/
#
# Same as BA9N but returns positions, not just counts. Uses the full BWT + SA
# pipeline with precomputed suffix array for O(|pattern|) lookup per pattern.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9o.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip() + '$'
    patterns = [l.strip() for l in lines[1:] if l.strip()]
    n = len(text)
    sa = sorted(range(n), key=lambda i: text[i:])
    bwt = ''.join(text[sa[i]-1] if sa[i]>0 else text[-1] for i in range(n))
    first = sorted(bwt)
    first_occ = {}
    for i, ch in enumerate(first):
        if ch not in first_occ: first_occ[ch] = i
    # Precompute count arrays
    counts = defaultdict(lambda: [0]*(n+1))
    for i, ch in enumerate(bwt):
        for c in list(counts.keys()): counts[c][i+1] = counts[c][i]
        counts[ch][i+1] = counts[ch][i] + 1

    positions = set()
    for pattern in patterns:
        top, bottom = 0, n-1
        for i in range(len(pattern)-1, -1, -1):
            symbol = pattern[i]
            if symbol not in first_occ: bottom = -1; break
            top = first_occ[symbol] + counts[symbol][top]
            bottom = first_occ[symbol] + counts[symbol][bottom+1] - 1
            if top > bottom: bottom = -1; break
        if top <= bottom:
            for i in range(top, bottom+1):
                positions.add(sa[i])

    print(' '.join(map(str, sorted(positions))))

if __name__ == '__main__': solve(get_input())
