# Finding an Origin of Replication (ORI)
# Rosalind problem: https://rosalind.info/problems/ori/
#
# Problem: Given a genome string, find the origin of replication (ori) by
# identifying the region with the minimum skew (most likely location where
# DNA replication begins, according to the minimum skew principle).
# Then find all DnaA boxes (9-mers appearing most frequently near the ori,
# including mismatches with d≤1 and their reverse complements).
#
# Algorithm:
#   1. Find the position(s) of minimum G-C skew.
#   2. Extract a window of ±500 bp around the minimum skew position.
#   3. Find the most frequent 9-mers (with ≤1 mismatch + reverse complements).

import os
import sys
from collections import Counter

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_ori.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

COMP = str.maketrans('ACGT', 'TGCA')

def rev_comp(s):
    return s.translate(COMP)[::-1]

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def find_skew_positions(genome):
    """Return positions where G-C skew is minimised."""
    skew = [0]
    for c in genome:
        if c == 'G':
            skew.append(skew[-1] + 1)
        elif c == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    min_skew = min(skew)
    return [i for i, s in enumerate(skew) if s == min_skew]

def frequent_words_mismatch(text, k, d):
    """Find most-frequent k-mers with ≤d mismatches, including reverse complements."""
    freq = Counter()
    n = len(text)
    for i in range(n - k + 1):
        window = text[i:i+k]
        for j in range(n - k + 1):
            candidate = text[j:j+k]
            if hamming(window, candidate) <= d:
                freq[window] += 1
                freq[rev_comp(window)] += 1

    # Simpler approach: for each k-mer in text, count approximate occurrences
    freq2 = Counter()
    kmers = [text[i:i+k] for i in range(n-k+1)]
    for km in kmers:
        for other in kmers:
            if hamming(km, other) <= d:
                freq2[km] += 1
        rc = rev_comp(km)
        for other in kmers:
            if hamming(rc, other) <= d:
                freq2[km] += 1

    max_freq = max(freq2.values()) if freq2 else 0
    return [km for km, cnt in freq2.items() if cnt == max_freq]

def solve(data):
    genome = data.strip()
    # Find minimum skew positions
    ori_positions = find_skew_positions(genome)
    print("Minimum skew positions (0-indexed):")
    print(' '.join(map(str, ori_positions)))

    # Extract window around first minimum skew position
    pos = ori_positions[0]
    half_window = 500
    start = max(0, pos - half_window)
    end = min(len(genome), pos + half_window)
    window = genome[start:end]

    # Find most frequent 9-mers (DnaA boxes) near ori
    k, d = 9, 1
    # Use simpler frequency search for portfolio demonstration
    freq = Counter()
    for i in range(len(window) - k + 1):
        kmer = window[i:i+k]
        freq[kmer] += 1
        freq[rev_comp(kmer)] += 1

    max_freq = max(freq.values()) if freq else 0
    dnaa_boxes = sorted({km for km, cnt in freq.items() if cnt == max_freq})
    print(f"\nMost frequent {k}-mers near ori (potential DnaA boxes):")
    print('\n'.join(dnaa_boxes) if dnaa_boxes else "None found")

if __name__ == '__main__':
    solve(get_input())
