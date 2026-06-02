# BA3B — Reconstruct a String from its Genome Path
# https://rosalind.info/problems/ba3b/
#
# Given: a list of k-mers forming a genome path (each adjacent pair overlaps by k-1).
# Return: the string that spells this genome path.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3b.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]
    genome = kmers[0]
    for kmer in kmers[1:]:
        genome += kmer[-1]   # each consecutive k-mer adds one new character
    print(genome)

if __name__ == '__main__': solve(get_input())
