# Inferring Protein from Spectrum (SPEC)
# Rosalind problem: https://rosalind.info/problems/spec/
#
# Problem: Given a list of masses from a protein's "prefix spectrum" (masses of
# all prefix sub-peptides), infer the protein string. The difference between
# consecutive prefix masses equals the monoisotopic mass of the next amino acid.
#
# Algorithm:
#   1. Sort the masses (they are already given in order but sort to be safe).
#   2. Compute differences between consecutive masses.
#   3. For each difference, look up the closest amino acid mass (within tolerance).
#
# Tolerance: 0.01 Da is sufficient for distinguishing all 20 amino acids.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_spec.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

# Monoisotopic residue masses
MONO_MASS = {
    'A': 71.03711,  'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146,  'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276,  'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333,
}

# Build reverse lookup: mass (rounded to 5 decimals) → amino acid
MASS_TO_AA = {}
for aa, m in MONO_MASS.items():
    key = round(m, 5)
    if key not in MASS_TO_AA:   # I and L have the same mass; prefer I
        MASS_TO_AA[key] = aa

def closest_aa(diff):
    """Find the amino acid whose mass is closest to diff (within 0.02 Da)."""
    best_aa, best_dist = None, float('inf')
    for aa, m in MONO_MASS.items():
        d = abs(diff - m)
        if d < best_dist:
            best_dist = d
            best_aa = aa
    return best_aa if best_dist < 0.02 else None

def solve(data):
    masses = sorted(float(x) for x in data.split())
    protein = []
    for i in range(1, len(masses)):
        diff = masses[i] - masses[i-1]
        aa = closest_aa(diff)
        if aa:
            protein.append(aa)
    print(''.join(protein))

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
