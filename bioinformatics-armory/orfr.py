# Finding Genes with ORFs (ORFR)
# Rosalind problem: https://rosalind.info/problems/orfr/
#
# Problem: Given a DNA string, find the longest protein string that can be
# translated from an open reading frame of s (considering all 6 reading frames,
# including the reverse complement).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_orfr.txt')
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

COMPLEMENT = str.maketrans('ACGT', 'TGCA')

def rev_comp(seq):
    return seq[::-1].translate(COMPLEMENT)

def find_orfs(seq):
    proteins = []
    for frame in range(3):
        i = frame
        while i + 3 <= len(seq):
            codon = seq[i:i+3]
            if codon == 'ATG':
                protein = []
                j = i
                while j + 3 <= len(seq):
                    aa = CODON_TABLE.get(seq[j:j+3], '')
                    if aa == '*':
                        proteins.append(''.join(protein))
                        break
                    protein.append(aa)
                    j += 3
            i += 3
    return proteins

def solve(data):
    seq = ''.join(line.strip() for line in data.splitlines()
                  if not line.startswith('>')).upper()
    candidates = find_orfs(seq) + find_orfs(rev_comp(seq))
    if candidates:
        print(max(candidates, key=len))

if __name__ == '__main__':
    solve(get_input())
