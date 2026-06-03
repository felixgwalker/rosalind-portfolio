# Introduction to the Bioinformatics Armory (INI)
# Rosalind problem: https://rosalind.info/problems/ini/
#
# Problem: Given a FASTA file with at most 10 DNA strings, count how many
# records it contains and print the count, then print the length of the
# shortest and longest sequences.
#
# This introductory problem familiarises users with FASTA format and the
# command-line bioinformatics workflow.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-armory', 'rosalind_ini.txt')
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
        print(0)
        return
    lengths = [len(seq) for _, seq in records]
    print(len(records))
    print(min(lengths))
    print(max(lengths))

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
