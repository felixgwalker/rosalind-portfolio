# Complementing a Strand of DNA (RVCO)
# Rosalind problem: https://rosalind.info/problems/rvco/
#
# Problem: Given a FASTA file containing DNA strings, return the number of
# records whose sequence is the reverse complement of another record in the file.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_rvco.txt')
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

COMPLEMENT = str.maketrans('ACGTacgt', 'TGCAtgca')

def rev_comp(seq):
    return seq[::-1].translate(COMPLEMENT)

def solve(data):
    records = parse_fasta(data)
    seqs = {seq for _, seq in records}
    count = sum(1 for _, seq in records if rev_comp(seq) in seqs)
    print(count)

if __name__ == '__main__':
    solve(get_input())
