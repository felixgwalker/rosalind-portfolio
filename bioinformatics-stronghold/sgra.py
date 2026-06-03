# Using the Spectrum Graph to Infer Peptides (SGRA)
# Rosalind problem: https://rosalind.info/problems/sgra/
#
# Problem: Given a weighted spectrum (list of fragment masses), build a spectrum
# graph where nodes are masses and there is an edge from m1 to m2 if
# m2 - m1 equals the monoisotopic mass of some amino acid. Find the longest
# path from the smallest mass to the largest mass in this DAG.
#
# The path spells out the peptide sequence (edge labels = amino acids).
#
# Algorithm: Topological sort + DP on the DAG of masses. O(n² · 20).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_sgra.txt')
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
TOL = 0.02   # tolerance for mass matching

def closest_aa(diff):
    best_aa, best_dist = None, float('inf')
    for aa, m in MONO_MASS.items():
        d = abs(diff - m)
        if d < best_dist:
            best_dist = d
            best_aa = aa
    return (best_aa, best_dist) if best_dist < TOL else (None, TOL)

def solve(data):
    masses = sorted(float(x) for x in data.split())
    n = len(masses)

    # dp[i] = (best path length ending at masses[i], previous index, edge label)
    dp = [0] * n
    prev = [-1] * n
    label = [''] * n

    for j in range(1, n):
        for i in range(j):
            diff = masses[j] - masses[i]
            aa, dist = closest_aa(diff)
            if aa and dp[i] + 1 > dp[j]:
                dp[j] = dp[i] + 1
                prev[j] = i
                label[j] = aa

    # Reconstruct path from largest mass (last node)
    end = n - 1
    path = []
    while prev[end] != -1:
        path.append(label[end])
        end = prev[end]

    print(''.join(reversed(path)))

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
