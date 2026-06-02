# BA3E — Construct the De Bruijn Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3e/
#
# Given: a list of k-mers.
# Return: the De Bruijn graph adjacency list: for each k-mer, add edge prefix → suffix.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3e.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]
    adj = defaultdict(list)
    for kmer in kmers:
        adj[kmer[:-1]].append(kmer[1:])
    for node in sorted(adj):
        print(f"{node} -> {','.join(adj[node])}")

if __name__ == '__main__': solve(get_input())
