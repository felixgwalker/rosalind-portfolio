# Protein Translation (PTRA)
# Rosalind problem: https://rosalind.info/problems/ptra/
#
# Problem: Given a DNA string s and a protein string p, find all substrings of
# s (or its reverse complement) that encode p as a protein. Output each such
# substring (as the DNA coding sequence), one per line.
#
# Algorithm: For each position in s (and reverse complement), try all 3 reading
# frames. When an ATG is found, translate until stop and compare to p.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_ptra.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

DNA_CODON = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
    'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
    'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
    'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'Stop','TAG':'Stop',
    'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
    'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'Stop','TGG':'W',
    'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}

COMP = str.maketrans('ACGT', 'TGCA')

def rev_comp(s):
    return s.translate(COMP)[::-1]

def find_encodings(dna, protein):
    """Find all substrings of dna that encode protein (including partial ORFs)."""
    results = []
    plen = len(protein)
    for start in range(len(dna) - plen * 3 + 1):
        subseq = dna[start:start + plen * 3]
        translated = []
        valid = True
        for i in range(0, len(subseq), 3):
            codon = subseq[i:i+3]
            aa = DNA_CODON.get(codon, '')
            if aa == 'Stop' or not aa:
                valid = False
                break
            translated.append(aa)
        if valid and ''.join(translated) == protein:
            results.append(subseq)
    return results

def solve(data):
    lines = data.splitlines()
    s = lines[0].strip()
    p = lines[1].strip()

    results = find_encodings(s, p)
    results += find_encodings(rev_comp(s), p)

    for r in results:
        print(r)

if __name__ == '__main__':
    solve(get_input())
