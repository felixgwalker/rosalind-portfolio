# Computing GC Content (GC)
# Rosalind problem: https://rosalind.info/problems/gc/
#
# Problem: Given a FASTA file with at most 10 DNA strings, find the ID of the
# sequence with the highest GC content (percentage of G and C bases) and print
# that ID followed by the GC% to at least 6 decimal places.
#
# Algorithm:
#   1. Parse FASTA: accumulate sequence lines between ">" headers.
#   2. For each sequence: GC% = (count('G') + count('C')) / len * 100
#   3. Linear scan to find the maximum.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_gc.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    """Return list of (id, sequence) tuples from a FASTA string."""
    records = []
    current_id = None
    parts = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if current_id is not None:
                records.append((current_id, ''.join(parts)))
            current_id = line[1:]   # strip the ">" prefix
            parts = []
        else:
            parts.append(line)
    if current_id is not None:
        records.append((current_id, ''.join(parts)))
    return records

def gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

def solve(data):
    records = parse_fasta(data)
    best_id = None
    best_gc = -1.0
    for seq_id, seq in records:
        gc = gc_content(seq)
        if gc > best_gc:
            best_gc = gc
            best_id = seq_id
    print(best_id)
    print(f"{best_gc:.6f}")

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
