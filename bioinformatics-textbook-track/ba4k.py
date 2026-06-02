# BA4K — Compute the Score of a Linear Peptide Against a Spectrum
# https://rosalind.info/problems/ba4k/
#
# Given: An amino acid string Peptide and a collection of integers Spectrum.
# Return: The linear peptide score of Peptide with respect to Spectrum.

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba4k.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

MASSES = {
    'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
    'N':114,'D':115,'Q':128,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
}

def linear_spectrum(peptide):
    masses = [MASSES[aa] for aa in peptide]
    n = len(masses)
    prefix = [0] * (n + 1)
    for i in range(n): prefix[i+1] = prefix[i] + masses[i]
    spec = [0]
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            spec.append(prefix[start + length] - prefix[start])
    return sorted(spec)

def score_linear(peptide, spectrum):
    pep_spec = Counter(linear_spectrum(peptide))
    sp = Counter(spectrum)
    return sum(min(pep_spec[m], sp[m]) for m in pep_spec)

def solve(data):
    lines = data.splitlines()
    peptide = lines[0].strip()
    spectrum = list(map(int, lines[1].split()))
    print(score_linear(peptide, spectrum))

if __name__ == '__main__': solve(get_input())
