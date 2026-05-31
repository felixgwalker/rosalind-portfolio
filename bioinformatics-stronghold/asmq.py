# Assessing Assembly Quality with N50 and N75 (ASMQ)
# Rosalind problem: https://rosalind.info/problems/asmq/
#
# Problem: Given a FASTA file of contigs, compute the N50 and N75 statistics.
# N_x is the length L such that contigs of length ≥ L cover at least x% of the
# total assembly length. It summarises assembly contiguity: larger N50 = better.
#
# Algorithm:
#   1. Sort contigs by length descending.
#   2. Accumulate lengths; N50 is the length where cumulative sum ≥ 0.5 × total.
#   3. Similarly for N75 (cumulative ≥ 0.75 × total).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_asmq.txt')
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

def nx_stat(lengths, x):
    """Compute Nx statistic for sorted (descending) lengths."""
    total = sum(lengths)
    threshold = total * x / 100
    cumsum = 0
    for L in lengths:
        cumsum += L
        if cumsum >= threshold:
            return L
    return lengths[-1]

def solve(data):
    seqs = parse_fasta(data)
    lengths = sorted((len(s) for s in seqs), reverse=True)
    print(nx_stat(lengths, 50))
    print(nx_stat(lengths, 75))

if __name__ == '__main__':
    solve(get_input())
