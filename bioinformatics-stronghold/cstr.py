# Creating a Character-Based Phylogeny (CSTR)
# Rosalind problem: https://rosalind.info/problems/cstr/
#
# Problem: Given a FASTA alignment of n taxa and m columns, each column defines
# a "character" — a bipartition of taxa based on their symbol at that position.
# Find all non-trivial bipartitions (neither side empty, neither side a singleton
# that's unique — only two distinct symbols, each on at least 2 taxa) and output
# the character table (bipartitions as binary strings).
#
# Output: One binary string per valid character; '1' = one state, '0' = other.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_cstr.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    records = []
    current_id, parts = None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if current_id is not None:
                records.append((current_id, ''.join(parts)))
            current_id, parts = line[1:], []
        else:
            parts.append(line)
    if current_id is not None:
        records.append((current_id, ''.join(parts)))
    return records

def solve(data):
    records = parse_fasta(data)
    if not records:
        return
    n = len(records)
    seqs = [seq for _, seq in records]
    m = len(seqs[0])
    seen = set()

    for col in range(m):
        column = [seq[col] for seq in seqs]
        symbols = set(column)
        if len(symbols) != 2:
            continue   # only process columns with exactly 2 distinct symbols

        s0, s1 = sorted(symbols)
        bits = ''.join('0' if c == s0 else '1' for c in column)
        # Avoid duplicates and ensure neither partition is trivial (all same)
        complement = ''.join('1' if b == '0' else '0' for b in bits)
        canonical = min(bits, complement)
        if canonical not in seen:
            seen.add(canonical)
            print(canonical)

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
