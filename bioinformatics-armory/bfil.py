# Base Filtration by Quality (BFIL)
# Rosalind problem: https://rosalind.info/problems/bfil/
#
# Problem: Given a FASTQ file and a quality threshold q, filter out reads that
# contain any base with Phred quality score below q. Output the surviving reads
# in FASTQ format.
#
# FASTQ format: 4 lines per read:
#   @header
#   sequence
#   + (separator)
#   quality string (ASCII, Phred+33 encoding)
#
# Phred score = ord(quality_char) - 33

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_bfil.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    # First line is the quality threshold
    threshold = int(lines[0].strip())
    output = []

    i = 1
    while i + 3 <= len(lines):
        header = lines[i]
        seq = lines[i+1]
        plus = lines[i+2]
        qual = lines[i+3]
        i += 4

        # Check all base quality scores
        min_qual = min(ord(c) - 33 for c in qual)
        if min_qual >= threshold:
            output.extend([header, seq, plus, qual])

    print('\n'.join(output))

if __name__ == '__main__':
    solve(get_input())
