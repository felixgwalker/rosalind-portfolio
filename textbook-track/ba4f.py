# BA4F — Compute the Score of a Cyclic Peptide Against a Spectrum
# https://rosalind.info/problems/ba4f/
#
# Given: a cyclic peptide (space-separated masses) and a spectrum.
# Return: the score = number of masses in the theoretical spectrum that also appear
# in the given spectrum (counting multiplicity).

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba4f.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def cyclic_spectrum(masses):
    n = len(masses)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + masses[i]
    total = prefix[n]
    spec = [0, total]
    for length in range(1, n):
        for start in range(n):
            if start + length <= n:
                spec.append(prefix[start+length] - prefix[start])
            else:
                spec.append(total - prefix[start] + prefix[start+length-n])
    return sorted(spec)

def score(peptide_masses, spectrum):
    theo = Counter(cyclic_spectrum(peptide_masses))
    real = Counter(spectrum)
    return sum(min(theo[m], real[m]) for m in theo)

def solve(data):
    lines = data.splitlines()
    peptide = list(map(int, lines[0].split()))
    spectrum = list(map(int, lines[1].split()))
    print(score(peptide, spectrum))

if __name__ == '__main__': solve(get_input())
