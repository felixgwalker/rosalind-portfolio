# Base Quality Distribution (BPHR)
# Rosalind problem: https://rosalind.info/problems/bphr/
#
# Problem: Given a FASTQ file and a quality threshold q (Phred score), determine
# for each read position the proportion of bases with quality below the threshold.
# Output: For each position where any read had quality < q, print the 1-based
# position and the proportion of reads where quality was below q.
#
# FASTQ format: Each read = 4 lines (header, sequence, '+', quality string).
# Phred+33 encoding: quality = ord(char) - 33.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_bphr.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    # First line is the quality threshold
    threshold = int(lines[0].strip())
    reads = []

    # Parse FASTQ records (4 lines each) starting from line 1
    i = 1
    while i < len(lines):
        if lines[i].startswith('@'):
            seq_line = lines[i+1].strip() if i+1 < len(lines) else ''
            qual_line = lines[i+3].strip() if i+3 < len(lines) else ''
            if qual_line:
                reads.append(qual_line)
            i += 4
        else:
            i += 1

    if not reads:
        return

    read_len = max(len(r) for r in reads)
    n_reads = len(reads)

    for pos in range(read_len):
        below = sum(1 for r in reads if pos < len(r) and (ord(r[pos]) - 33) < threshold)
        prop = below / n_reads
        if below > 0:
            print(pos + 1, round(prop, 3))

if __name__ == '__main__':
    solve(get_input())
