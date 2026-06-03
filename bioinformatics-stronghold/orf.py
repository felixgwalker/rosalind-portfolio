# Open Reading Frames (ORF)
# Rosalind problem: https://rosalind.info/problems/orf/
#
# Problem: Given a DNA string in FASTA format, find every distinct protein that
# can be encoded by an ORF in any of the 6 reading frames (3 on the forward
# strand, 3 on the reverse complement strand). An ORF starts at ATG and ends
# at the first downstream stop codon in the same frame.
#
# Output: All distinct candidate protein strings, one per line (any order).
#
# Algorithm:
#   1. Check all 6 frames (3 forward + 3 on reverse complement).
#   2. For each frame, scan for ATG start codons.
#   3. From each ATG, translate codon by codon until a stop codon is hit.
#   4. Collect results in a set to deduplicate.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_orf.txt')
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

# DNA codon table (T not U since input is DNA)
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

COMP = str.maketrans('ACGTacgt', 'TGCAtgca')

def reverse_complement(dna):
    return dna.translate(COMP)[::-1]

def find_orfs(dna):
    """Return the set of all protein strings encoded by ORFs in dna."""
    proteins = set()
    n = len(dna)
    for start in range(n):
        if dna[start:start+3] != 'ATG':
            continue
        # Translate from this start codon until stop or end of string
        protein = []
        for j in range(start, n - 2, 3):
            codon = dna[j:j+3]
            aa = DNA_CODON.get(codon, '')
            if aa == 'Stop':
                proteins.add(''.join(protein))
                break
            if aa:
                protein.append(aa)
    return proteins

def solve(data):
    dna = parse_fasta(data)
    # Search both strands
    all_proteins = find_orfs(dna) | find_orfs(reverse_complement(dna))
    for p in sorted(all_proteins):
        print(p)

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
