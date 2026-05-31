# BA3D — Construct the De Bruijn Graph of a String
# https://rosalind.info/problems/ba3d/
#
# Given: an integer k and a DNA string Text.
# Return: the adjacency list of the De Bruijn graph Debruijn_k(Text).
# For each k-mer in Text, add an edge from its (k-1)-prefix to its (k-1)-suffix.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3d.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    k, text = int(lines[0].strip()), lines[1].strip()
    adj = defaultdict(set)
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        adj[kmer[:-1]].add(kmer[1:])
    for node in sorted(adj):
        print(f"{node} -> {','.join(sorted(adj[node]))}")

if __name__ == '__main__': solve(get_input())
