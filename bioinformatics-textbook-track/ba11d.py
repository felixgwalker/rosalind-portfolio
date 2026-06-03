# BA11D — Convert a Peptide Vector into a Peptide
# https://rosalind.info/problems/ba11d/
#
# Given: A {0,1} vector v (space-separated) of length n.
# Return: The amino acid string Peptide whose peptide vector is v.
#         ParentMass = n + 1; prefix masses are the (1-indexed) positions
#         where v[i] = 1, plus 0 at the start and ParentMass at the end.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba11d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MASS_TO_AA = {
    57:'G', 71:'A', 87:'S', 97:'P', 99:'V', 101:'T', 103:'C',
    113:'L', 114:'N', 115:'D', 128:'Q', 129:'E', 131:'M',
    137:'H', 147:'F', 156:'R', 163:'Y', 186:'W'
}

def vector_to_peptide(vector):
    n = len(vector)
    parent = n + 1
    prefix_masses = [0] + [i + 1 for i, v in enumerate(vector) if v == 1] + [parent]
    peptide = []
    for i in range(len(prefix_masses) - 1):
        diff = prefix_masses[i + 1] - prefix_masses[i]
        peptide.append(MASS_TO_AA.get(diff, '?'))
    return ''.join(peptide)

def solve(data):
    vector = list(map(int, data.split()))
    print(vector_to_peptide(vector))

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
