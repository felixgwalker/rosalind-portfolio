# Calculating Protein Mass (PRTM)
# Rosalind problem: https://rosalind.info/problems/prtm/
#
# Problem: Given a protein string of length at most 1000, compute its
# monoisotopic mass: the sum of the monoisotopic masses of each constituent
# amino acid residue (i.e., after peptide bond formation — water is excluded
# for internal residues and only one water molecule is added for the full chain,
# but Rosalind's mass table already gives residue masses, so just sum them).
#
# Output: The total mass rounded to 3 decimal places.
#
# Note: The monoisotopic mass table uses the most common isotope of each element.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_prtm.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

# Monoisotopic residue masses (Da) from the Rosalind mass table
MONO_MASS = {
    'A': 71.03711,  'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146,  'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276,  'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333,
}

def solve(data):
    protein = data.strip()
    total = sum(MONO_MASS[aa] for aa in protein)
    print(round(total, 3))

if __name__ == '__main__':
    solve(get_input())
