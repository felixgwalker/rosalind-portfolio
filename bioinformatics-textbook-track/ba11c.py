# BA11C — Convert a Peptide into a Peptide Vector
# https://rosalind.info/problems/ba11c/
#
# Given: An amino acid string Peptide.
# Return: The peptide vector of Peptide: a {0,1} vector v of length
#         ParentMass(Peptide) - 1 where v[i] = 1 iff (i+1) is a prefix mass.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba11c.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MASSES = {
    'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
    'N':114,'D':115,'Q':128,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
}

def peptide_to_vector(peptide):
    masses = [MASSES[aa] for aa in peptide]
    total = sum(masses)
    vector = [0] * (total - 1)
    prefix = 0
    for m in masses[:-1]:
        prefix += m
        vector[prefix - 1] = 1  # position prefix (1-indexed) maps to index prefix-1
    return vector

def solve(data):
    peptide = data.strip()
    print(' '.join(map(str, peptide_to_vector(peptide))))

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
