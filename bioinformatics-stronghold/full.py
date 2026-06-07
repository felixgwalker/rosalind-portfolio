# Inferring Peptide from Full Spectrum (FULL)
# Rosalind problem: https://rosalind.info/problems/full/
#
# Problem: Given a "full" mass spectrum (containing both prefix and suffix
# masses as well as the total/parent mass), reconstruct the peptide.
#
# The full spectrum of peptide a1..an contains:
#   0, m1, m1+m2, ..., M  (prefix masses, M = total/parent mass)
#   0, m_n, m_n+m_{n-1}, ..., M  (suffix masses)
# where mi = mass of residue i.
#
# Input format: the first number L[0] is the parent mass M; the rest of the
# numbers are the remaining (internal) prefix and suffix masses.
#
# Note: complement pairing alone (w, M-w both present) cannot distinguish
# prefix masses from suffix masses, since the complete spectrum is symmetric
# -- every internal prefix mass's complement is an internal suffix mass and
# vice versa, so essentially *every* mass has a complement in the set.
#
# Algorithm (spectral graph):
#   1. M = L[0]; build the node set S = {0, M} u (the rest of L).
#   2. Connect u -> v (u < v) when v - u is close to some amino acid's mass;
#      label the edge with that amino acid.
#   3. The true prefix-mass chain is a path from 0 to M with exactly
#      n = len(S)/2 edges (n = number of residues). Search for such a path
#      and read off the edge labels to get the peptide.

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
TOLERANCE = 0.02

def closest_aa(diff):
    best_aa, best_dist = None, float('inf')
    for aa, m in MONO_MASS.items():
        d = abs(diff - m)
        if d < best_dist:
            best_dist = d
            best_aa = aa
    return best_aa if best_dist < TOLERANCE else None

def solve(data):
    nums = [float(x) for x in data.split()]
    M = nums[0]               # parent mass
    n = (len(nums) - 3) // 2  # |L| = 2n + 3, so this recovers the peptide length

    # The b-ion and y-ion masses (in no particular order). Each is an unknown
    # residue-weight sum plus an unknown constant offset (w1 for b-ions, w2 for
    # y-ions): b_i = w(prefix_i) + w1, y_j = w(suffix_j) + w2. Either way,
    # *consecutive* ions in a chain differ by exactly one residue's mass, so the
    # offsets cancel out and we can recover the peptide from mass differences.
    masses = sorted(set(nums[1:]))

    # Spectral graph: edge u -> v (u < v) labelled with the amino acid whose
    # mass equals v - u (within tolerance).
    edges = {m: [] for m in masses}
    for i, u in enumerate(masses):
        for v in masses[i + 1:]:
            aa = closest_aa(v - u)
            if aa:
                edges[u].append((v, aa))

    # The b-ion chain b_0 < b_1 < ... < b_n (b_0 = w1, the smallest b-ion mass)
    # is a path of exactly n edges whose labels spell the peptide in order. The
    # smallest mass overall is min(w1, w2); Rosalind's datasets are built so it
    # is w1, i.e. the b-ion chain starts at the smallest mass in the spectrum.
    path = []

    def search(node, depth):
        if depth == n:
            return True
        for nxt, aa in edges[node]:
            path.append(aa)
            if search(nxt, depth + 1):
                return True
            path.pop()
        return False

    search(masses[0], 0)
    print(''.join(path))

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
