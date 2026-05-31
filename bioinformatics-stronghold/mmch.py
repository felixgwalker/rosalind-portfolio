# Maximum Matchings and RNA Secondary Structures (MMCH)
# Rosalind problem: https://rosalind.info/problems/mmch/
#
# Problem: Given an RNA string s (≤ 100 nt), return the total number of maximum
# matchings of nucleotide bases in its bonding graph (where A pairs with U and
# G pairs with C, no crossing constraint).
#
# Formula: A maximum matching pairs min(nA, nU) A-U bonds and min(nG, nC) G-C bonds.
# The number of ways to achieve this maximum:
#   P(max(nA,nU), min(nA,nU))  ×  P(max(nG,nC), min(nG,nC))
# where P(n, k) = n! / (n-k)! is the partial permutation count.
#
# Reasoning: Choose which min(nA,nU) of the larger group to pair, then match
# them with the smaller group in all possible orders.

import os
import sys
from math import factorial

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_mmch.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        if not line.startswith('>'):
            parts.append(line.strip())
    return ''.join(parts)

def partial_perm(n, k):
    """P(n, k) = n! / (n-k)!  (number of ways to choose ordered k items from n)."""
    if k > n:
        return 0
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result

def solve(data):
    rna = parse_fasta(data)
    nA, nU = rna.count('A'), rna.count('U')
    nG, nC = rna.count('G'), rna.count('C')

    # Maximum A-U pairs = min(nA, nU); ways = P(larger, smaller)
    au = partial_perm(max(nA, nU), min(nA, nU))
    # Maximum G-C pairs = min(nG, nC); ways = P(larger, smaller)
    gc = partial_perm(max(nG, nC), min(nG, nC))

    print(au * gc)

if __name__ == '__main__':
    solve(get_input())
