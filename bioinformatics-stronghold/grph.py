# Overlap Graphs (GRPH)
# Rosalind problem: https://rosalind.info/problems/grph/
#
# Problem: Given a collection of DNA strings in FASTA format, construct a
# directed overlap graph with overlap length k = 3: draw an edge from sequence
# s to sequence t (s ≠ t) if the last 3 bases of s equal the first 3 bases of t.
#
# Output: one edge per line as "ID_s ID_t" (order matters — directed).
#
# Algorithm: O(n²·k) — for each ordered pair of distinct sequences check the
# suffix/prefix condition. k is fixed at 3 so the check is O(1) effectively.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_grph.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read(), None

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
    k = 3
    edges = []
    for i, (id_a, seq_a) in enumerate(records):
        suffix_a = seq_a[-k:]       # last k bases of sequence a
        for j, (id_b, seq_b) in enumerate(records):
            if i == j:
                continue            # no self-loops
            if suffix_a == seq_b[:k]:   # last k of a == first k of b
                edges.append(f"{id_a} {id_b}")
    print('\n'.join(edges))

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
