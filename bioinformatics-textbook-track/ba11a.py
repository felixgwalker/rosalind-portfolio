# BA11A — Construct the Graph of a Spectrum
# https://rosalind.info/problems/ba11a/
#
# Given: A collection of integers Spectrum.
# Return: The spectrum graph of Spectrum: for every pair of masses in Spectrum
#         whose difference equals an amino acid mass, output an edge labeled
#         with the corresponding amino acid(s).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba11a.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

# Integer amino acid masses used in Chapter 11 (same as Chapter 4).
MASS_TO_AA = {
    57:'G', 71:'A', 87:'S', 97:'P', 99:'V', 101:'T', 103:'C',
    113:'L', 114:'N', 115:'D', 128:'Q', 129:'E', 131:'M',
    137:'H', 147:'F', 156:'R', 163:'Y', 186:'W'
}
# I has the same mass as L; K has the same mass as Q — use canonical choice.

def solve(data):
    spectrum = sorted(set(map(int, data.split())))
    if 0 not in spectrum:
        spectrum = [0] + spectrum
    for i in range(len(spectrum)):
        for j in range(i + 1, len(spectrum)):
            diff = spectrum[j] - spectrum[i]
            if diff in MASS_TO_AA:
                print(f"{spectrum[i]} -> {spectrum[j]}:{MASS_TO_AA[diff]}")

if __name__ == '__main__': solve(get_input())
