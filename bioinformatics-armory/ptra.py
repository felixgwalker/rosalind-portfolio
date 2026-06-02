# Protein Translation (PTRA)
# Rosalind problem: https://rosalind.info/problems/ptra/
#
# Problem: Given a DNA string s and a protein string p, find all substrings
# of s whose translation equals p.  Return the 1-based starting positions.
#
# Uses the standard (vertebrate mitochondrial) genetic code.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_ptra.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

def translate(dna):
    aa = []
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        amino = CODON_TABLE.get(codon, '?')
        if amino == '*':
            break
        aa.append(amino)
    return ''.join(aa)

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    dna = lines[0].upper()
    protein = lines[1].upper()
    # Length of DNA that encodes this protein (no stop codon included)
    needed = len(protein) * 3
    positions = []
    for i in range(len(dna) - needed + 1):
        if translate(dna[i:i + needed]) == protein:
            positions.append(str(i + 1))
    print('\n'.join(positions))

if __name__ == '__main__':
    solve(get_input())
