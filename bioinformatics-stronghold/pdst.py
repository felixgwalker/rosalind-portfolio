# Creating a Distance Matrix (PDST)
# Rosalind problem: https://rosalind.info/problems/pdst/
#
# Problem: Given a FASTA file with n equal-length DNA strings, compute the
# n×n p-distance matrix where entry (i, j) is the p-distance between sequences
# i and j: p(s, t) = (number of positions where they differ) / length.
#
# The p-distance is simply the Hamming distance normalised by sequence length.
# Output: n lines, each with n space-separated values (diagonal = 0).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_pdst.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read(), None

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

def p_distance(s, t):
    """Normalised Hamming distance between equal-length strings."""
    diffs = sum(a != b for a, b in zip(s, t))
    return diffs / len(s)

def solve(data):
    seqs = parse_fasta(data)
    n = len(seqs)
    for i in range(n):
        row = [f"{p_distance(seqs[i], seqs[j]):.5f}" for j in range(n)]
        print(' '.join(row))

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
