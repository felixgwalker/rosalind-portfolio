# BA4B — Find Substrings of a Genome Encoding a Given Amino Acid String
# https://rosalind.info/problems/ba4b/
#
# Given: a DNA string Text and an amino acid string Peptide.
# Return: all substrings of Text encoding Peptide (in any reading frame on either strand).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba4b.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

DNA_CODON = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'Stop','TAG':'Stop','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'Stop','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}
COMP = str.maketrans('ACGT','TGCA')

def rev_comp(s):
    return s.translate(COMP)[::-1]

def translate_dna(dna):
    result = []
    for i in range(0, len(dna) - 2, 3):
        aa = DNA_CODON.get(dna[i:i+3], '')
        if aa == 'Stop':
            break
        result.append(aa)
    return ''.join(result)

def solve(data):
    lines = data.splitlines()
    text, peptide = lines[0].strip(), lines[1].strip()
    L = len(peptide) * 3
    results = []
    for i in range(len(text) - L + 1):
        sub = text[i:i+L]
        if translate_dna(sub) == peptide or translate_dna(rev_comp(sub)) == peptide:
            results.append(sub)
    print('\n'.join(results))

if __name__ == '__main__': solve(get_input())
