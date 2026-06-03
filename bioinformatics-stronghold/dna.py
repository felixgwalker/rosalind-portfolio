# Counting DNA Nucleotides (DNA)
# Rosalind problem: https://rosalind.info/problems/dna/
#
# Problem: Given a DNA string of length at most 1000 nt, count the number of
# times each nucleotide A, C, G, T appears. Output the four counts separated
# by spaces in the order A C G T.
#
# Algorithm: Linear scan — O(n) time, O(1) space (fixed alphabet of 4).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_dna.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    dna = data.strip()
    # str.count is O(n) for each call; total still O(n)
    print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))

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
