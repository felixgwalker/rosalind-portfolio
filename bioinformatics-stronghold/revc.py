# Complementing a Strand of DNA (REVC)
# Rosalind problem: https://rosalind.info/problems/revc/
#
# Problem: Given a DNA string s, return its reverse complement. The reverse
# complement is the sequence read on the antiparallel complementary strand in
# the 5'→3' direction: complement each base (A↔T, G↔C) then reverse.
#
# Algorithm: Build a translation table for O(1) char lookups, join in one
# pass, then reverse. Overall O(n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_revc.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

# Watson-Crick complement mapping
COMP = str.maketrans('ACGTacgt', 'TGCAtgca')

def solve(data):
    dna = data.strip()
    # translate() applies the complement map, [::-1] reverses the result
    print(dna.translate(COMP)[::-1])

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
