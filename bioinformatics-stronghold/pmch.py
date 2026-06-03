# Perfect Matchings and RNA Secondary Structures (PMCH)
# Rosalind problem: https://rosalind.info/problems/pmch/
#
# Problem: Given an RNA string s having equal counts of A and U (nA = nU) and
# equal counts of G and C (nG = nC), compute the total number of perfect
# matchings of A-U and G-C base pairs (all possible pairings, including
# crossing ones).
#
# Formula: The number of perfect matchings = nA! × nG!
# Reasoning: Choose any bijection from the nA A-bases to the nU U-bases (nA! ways)
# and independently any bijection from the nG G-bases to the nC C-bases (nG! ways).
# All such bijections are valid pairings.

import os
import sys
from math import factorial

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_pmch.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        if not line.startswith('>'):
            parts.append(line.strip())
    return ''.join(parts)

def solve(data):
    rna = parse_fasta(data)
    nA = rna.count('A')   # equals count('U') by problem guarantee
    nG = rna.count('G')   # equals count('C') by problem guarantee
    print(factorial(nA) * factorial(nG))

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
