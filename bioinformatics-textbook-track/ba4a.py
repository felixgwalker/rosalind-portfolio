# BA4A — Translate an RNA String into an Amino Acid String
# https://rosalind.info/problems/ba4a/
#
# Given: an RNA string.
# Return: the protein encoded by the RNA (stopping at first stop codon).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4a.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'Stop','UAG':'Stop','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'Stop','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate(rna):
    protein = []
    for i in range(0, len(rna) - 2, 3):
        aa = CODON_TABLE.get(rna[i:i+3], '')
        if aa == 'Stop':
            break
        if aa:
            protein.append(aa)
    return ''.join(protein)

def solve(data):
    print(translate(data.strip()))

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
