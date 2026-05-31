# Consensus and Profile (CONS)
# Rosalind problem: https://rosalind.info/problems/cons/
#
# Problem: Given a FASTA file with at most 10 equal-length DNA strings, compute:
#   1. A profile matrix: 4 rows (A/C/G/T) × n columns, each cell = count of
#      that base at that column position across all sequences.
#   2. A consensus string: the base with the highest count at each column.
#
# Output format:
#   Consensus string on first line.
#   Then four rows: "A: c1 c2 ..." for bases A, C, G, T in that order.
#
# Algorithm: O(k·n) where k = number of sequences, n = their common length.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_cons.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    records, current_id, parts = [], None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if current_id is not None:
                records.append(''.join(parts))
            current_id = line[1:]
            parts = []
        else:
            parts.append(line)
    if current_id is not None:
        records.append(''.join(parts))
    return records

def solve(data):
    sequences = parse_fasta(data)
    n = len(sequences[0])

    # Profile matrix: counts per base per column position
    profile = {b: [0] * n for b in 'ACGT'}
    for seq in sequences:
        for i, base in enumerate(seq):
            profile[base][i] += 1

    # Consensus: most frequent base at each column (ACGT ordering breaks ties consistently)
    consensus = ''.join(max('ACGT', key=lambda b: profile[b][i]) for i in range(n))

    print(consensus)
    for base in 'ACGT':
        print(f"{base}: {' '.join(map(str, profile[base]))}")

if __name__ == '__main__':
    solve(get_input())
