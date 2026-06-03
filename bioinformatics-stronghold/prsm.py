# Matching a Spectrum to a Protein (PRSM)
# Rosalind problem: https://rosalind.info/problems/prsm/
#
# Problem: Given n protein strings and a collection of positive numbers
# (a mass spectrum), find the protein string P that maximises the number of
# elements of the spectrum that are prefix masses of P (within tolerance 0.01).
#
# A prefix mass of P is the sum of residue masses of a prefix P[0..k].
#
# Algorithm: For each protein, compute all prefix masses and count how many
# spectrum values appear (within tolerance). O(n · |proteins| · |spectrum|).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_prsm.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MONO_MASS = {
    'A': 71.03711,  'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146,  'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276,  'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333,
}

def prefix_masses(protein):
    masses = [0.0]
    for aa in protein:
        masses.append(masses[-1] + MONO_MASS[aa])
    return masses[1:]   # exclude 0

def score(protein, spectrum, tol=0.01):
    pm = set(round(m, 5) for m in prefix_masses(protein))
    count = 0
    for s in spectrum:
        for pm_val in pm:
            if abs(s - pm_val) <= tol:
                count += 1
                break
    return count

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    proteins = lines[1:n+1]
    spectrum = [float(x) for x in lines[n+1:] if x.strip()]

    best_protein = None
    best_score = -1
    for p in proteins:
        s = score(p.strip(), spectrum)
        if s > best_score:
            best_score = s
            best_protein = p.strip()

    print(best_score)
    print(best_protein)

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
