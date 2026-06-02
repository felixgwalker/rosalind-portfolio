# BA1J — Find Frequent Words with Mismatches and Reverse Complements
# https://rosalind.info/problems/ba1j/
#
# Same as BA1I but also count reverse complements of each approximate match.
# A k-mer Pattern is counted for each approximate occurrence of Pattern OR
# its reverse complement in Text.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1j.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

COMP = str.maketrans('ACGT', 'TGCA')

def rev_comp(s):
    return s.translate(COMP)[::-1]

def neighbors(pattern, d):
    if d == 0:
        yield pattern; return
    if not pattern:
        yield ''; return
    for rest in neighbors(pattern[1:], d):
        yield pattern[0] + rest
    for base in 'ACGT':
        if base != pattern[0]:
            for rest in neighbors(pattern[1:], d - 1):
                yield base + rest

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip()
    k, d = map(int, lines[1].split())
    n = len(text)
    freq = defaultdict(int)
    for i in range(n - k + 1):
        for nb in neighbors(text[i:i+k], d):
            freq[nb] += 1
            freq[rev_comp(nb)] += 1
    max_count = max(freq.values())
    print(' '.join(kmer for kmer, c in freq.items() if c == max_count))

if __name__ == '__main__': solve(get_input())
