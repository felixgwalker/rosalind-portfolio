# RNA Splicing (SPLC)
# Rosalind problem: https://rosalind.info/problems/splc/
#
# Problem: Given a FASTA file where the first sequence is a pre-mRNA (DNA
# encoding) and all remaining sequences are introns, remove all introns from
# the first sequence and translate the resulting exon-only mRNA into a protein.
#
# The introns can appear in any order and each appears exactly once.
#
# Algorithm:
#   1. Remove each intron substring from the DNA string (order doesn't matter
#      because introns don't overlap).
#   2. Replace T with U to get mRNA.
#   3. Translate using the standard codon table, stopping at the first stop codon.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_splc.txt')
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
                records.append(''.join(parts))
            current_id, parts = line[1:], []
        else:
            parts.append(line)
    if current_id is not None:
        records.append(''.join(parts))
    return records

CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
    'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
    'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
    'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
    'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'Stop','UAG':'Stop',
    'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
    'GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'Stop','UGG':'W',
    'CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate(rna):
    protein = []
    for i in range(0, len(rna) - 2, 3):
        aa = CODON_TABLE[rna[i:i+3]]
        if aa == 'Stop':
            break
        protein.append(aa)
    return ''.join(protein)

def solve(data):
    records = parse_fasta(data)
    dna = records[0]         # first record is the pre-mRNA (as DNA)
    introns = records[1:]    # remaining records are introns to remove

    for intron in introns:
        dna = dna.replace(intron, '')    # excise each intron

    rna = dna.replace('T', 'U')          # transcribe DNA → RNA
    print(translate(rna))

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
