# Inferring mRNA from Protein (MRNA)
# Rosalind problem: https://rosalind.info/problems/mrna/
#
# Problem: Given a protein string of length at most 1000, count how many
# different RNA strings could encode it, modulo 1,000,000.
#
# Algorithm: For each amino acid multiply the number of codons that encode it.
# Also multiply by 3 (for the three stop codons that must end the mRNA).
# All arithmetic done mod 10^6 to prevent overflow.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_mrna.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

# Number of codons encoding each amino acid (from the standard genetic code)
CODON_COUNT = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
    'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
    'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6,
    'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2,
}
STOP_CODONS = 3   # UAA, UAG, UGA

MOD = 1_000_000

def solve(data):
    protein = data.strip()
    result = STOP_CODONS   # start with stop codon choices
    for aa in protein:
        result = (result * CODON_COUNT[aa]) % MOD
    print(result)

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
