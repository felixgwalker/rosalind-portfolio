# Transitions and Transversions (TRAN)
# Rosalind problem: https://rosalind.info/problems/tran/
#
# Problem: Given two DNA strings s and t (in FASTA), aligned position by
# position, count transitions and transversions among positions where they differ,
# then return the ratio transitions / transversions.
#
# Definitions:
#   Transition:   A ↔ G  (purine  ↔ purine)   or  C ↔ T  (pyrimidine ↔ pyrimidine)
#   Transversion: A ↔ C, A ↔ T, G ↔ C, G ↔ T  (purine ↔ pyrimidine)
#
# Algorithm: Linear scan, classify each mismatch, accumulate counts. O(n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_tran.txt')
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
                records.append(''.join(parts))
            current_id, parts = line[1:], []
        else:
            parts.append(line)
    if current_id is not None:
        records.append(''.join(parts))
    return records

PURINES = {'A', 'G'}
PYRIMIDINES = {'C', 'T'}

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]

    transitions = 0
    transversions = 0

    for a, b in zip(s, t):
        if a == b:
            continue
        # Same chemical family = transition; different = transversion
        if (a in PURINES and b in PURINES) or (a in PYRIMIDINES and b in PYRIMIDINES):
            transitions += 1
        else:
            transversions += 1

    print(transitions / transversions)

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
