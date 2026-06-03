# Inferring Peptide from Full Spectrum (FULL)
# Rosalind problem: https://rosalind.info/problems/full/
#
# Problem: Given a "full" mass spectrum (containing both prefix and suffix
# masses as well as the total mass), reconstruct the peptide.
#
# The full spectrum of peptide a1..an contains:
#   0, m1, m1+m2, ..., M  (prefix masses, M = total)
#   0, m_n, m_n+m_{n-1}, ..., M  (suffix masses)
# where mi = mass of residue i.
#
# Algorithm:
#   1. The total mass M = max in the spectrum minus water (~18.01 Da for full protein).
#      Actually: given prefix masses, the total peptide mass M appears in the spectrum.
#   2. From the spectrum, identify pairs (w, M-w) to find prefix mass candidates.
#   3. Build prefix masses in increasing order; consecutive differences give amino acids.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_full.txt')
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
WATER = 18.01056   # mass of a water molecule added to a free peptide

def closest_aa(diff):
    best_aa, best_dist = None, float('inf')
    for aa, m in MONO_MASS.items():
        d = abs(diff - m)
        if d < best_dist:
            best_dist = d
            best_aa = aa
    return best_aa if best_dist < 0.02 else None

def solve(data):
    masses = sorted(float(x) for x in data.split())

    # Total peptide mass (the full spectrum includes mass M, which = last prefix mass)
    M = masses[-1]

    # Extract prefix masses: a mass w is a prefix mass if (M - w) also appears
    # (because M - prefix_w = corresponding suffix_w).
    mass_set = set(round(m, 5) for m in masses)

    prefix_masses = set()
    for m in masses:
        complement = round(M - m, 5)
        if complement in mass_set:
            prefix_masses.add(round(m, 5))

    prefix_masses = sorted(prefix_masses)

    # Consecutive differences of sorted prefix masses give amino acid residue masses
    protein = []
    for i in range(1, len(prefix_masses)):
        diff = prefix_masses[i] - prefix_masses[i-1]
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
