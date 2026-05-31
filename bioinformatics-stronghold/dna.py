# Counting DNA Nucleotides (DNA)
# Rosalind problem: https://rosalind.info/problems/dna/
#
# Problem: Given a DNA string of length at most 1000 nt, count the number of
# times each nucleotide A, C, G, T appears. Output the four counts separated
# by spaces in the order A C G T.
#
# Algorithm: Linear scan — O(n) time, O(1) space (fixed alphabet of 4).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_dna.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    dna = data.strip()
    # str.count is O(n) for each call; total still O(n)
    print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))

if __name__ == '__main__':
    solve(get_input())
