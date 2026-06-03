# Error Correction in Reads (CORR)
# Rosalind problem: https://rosalind.info/problems/corr/
#
# Problem: Given a collection of DNA reads, some appear multiple times (these
# are "correct") and some appear exactly once (these are "erroneous"). For each
# erroneous read, find a correct read that differs from it by exactly 1 substitution
# (Hamming distance 1), including reverse complements. Output the correction as
# "erroneous_read->corrected_read".
#
# Algorithm:
#   1. Build a set of correct reads (those appearing ≥ 2 times, plus their
#      reverse complements).
#   2. For each erroneous read, find the correct read at distance 1.

import os
import sys
from collections import Counter

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_corr.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    seqs = []
    parts = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if parts:
                seqs.append(''.join(parts))
            parts = []
        else:
            parts.append(line)
    if parts:
        seqs.append(''.join(parts))
    return seqs

COMP = str.maketrans('ACGT', 'TGCA')

def rev_comp(s):
    return s.translate(COMP)[::-1]

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def solve(data):
    reads = parse_fasta(data)
    freq = Counter(reads)

    # A read is "correct" if it (or its reverse complement) appears ≥ 2 times
    correct = set()
    for read, count in freq.items():
        if count >= 2:
            correct.add(read)
            correct.add(rev_comp(read))

    for read in reads:
        if freq[read] == 1 and read not in correct:
            # This read is erroneous — find its correction at Hamming distance 1
            rc = rev_comp(read)
            for cread in correct:
                if hamming(read, cread) == 1:
                    print(f"{read}->{cread}")
                    break
                if hamming(rc, cread) == 1:
                    print(f"{read}->{rev_comp(cread)}")
                    break

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
