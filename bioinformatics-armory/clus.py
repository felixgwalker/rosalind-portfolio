# Global Multiple Alignment (CLUS)
# Rosalind problem: https://rosalind.info/problems/clus/
#
# Problem: Given a FASTA file with DNA strings all of the same length,
# return the consensus string computed from the multiple alignment
# (majority base at each position; ties broken alphabetically).

import os
import sys
from collections import Counter

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_clus.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    records, cur_id, parts = [], None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if cur_id is not None:
                records.append((cur_id, ''.join(parts)))
            cur_id, parts = line[1:], []
        else:
            parts.append(line)
    if cur_id is not None:
        records.append((cur_id, ''.join(parts)))
    return records

def solve(data):
    records = parse_fasta(data)
    if not records:
        return
    seqs = [seq.upper() for _, seq in records]
    length = max(len(s) for s in seqs)
    consensus = []
    for i in range(length):
        col = [s[i] for s in seqs if i < len(s)]
        counts = Counter(col)
        best = max(sorted(counts), key=lambda b: counts[b])
        consensus.append(best)
    print(''.join(consensus))

if __name__ == '__main__':
    solve(get_input())
