# Finding the Longest Multiple Repeat (LREP)
# Rosalind problem: https://rosalind.info/problems/lrep/
#
# Problem: Given a DNA string s (≤ 1 Mbp in FASTA) and an integer k, find the
# longest substring of s that occurs at least k times.
#
# Algorithm: Binary search on answer length L + rolling hash to check.
#   For a given length L, use a dict of hashes to find any repeated substring
#   of exactly that length appearing ≥ k times. O(n log n) expected.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_lrep.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        if not line.startswith('>'):
            parts.append(line.strip())
    return ''.join(parts)

def find_repeated(s, L, k):
    """Return one substring of length L that appears >= k times, or ''."""
    from collections import defaultdict
    counts = defaultdict(int)
    n = len(s)
    for i in range(n - L + 1):
        sub = s[i:i+L]
        counts[sub] += 1
        if counts[sub] >= k:
            return sub
    return ''

def solve(data):
    lines = data.strip().splitlines()
    # First non-header line is k, then FASTA content
    # Actually format: line 1 = k (integer), remaining = FASTA
    # Let's handle both: if first non-empty line is a digit, it's k
    non_empty = [l.strip() for l in lines if l.strip()]
    if non_empty[0].isdigit():
        k = int(non_empty[0])
        fasta_text = '\n'.join(lines[1:])
    else:
        # FASTA first, then k on the last line
        fasta_text = '\n'.join(lines[:-1])
        k = int(lines[-1].strip())

    s = parse_fasta(fasta_text) if '>' in fasta_text else fasta_text.strip()

    # Binary search on length
    lo, hi = 1, len(s)
    best = ''
    while lo <= hi:
        mid = (lo + hi) // 2
        found = find_repeated(s, mid, k)
        if found:
            best = found
            lo = mid + 1
        else:
            hi = mid - 1

    print(best)

if __name__ == '__main__':
    solve(get_input())
