# BA3C — Construct the Overlap Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3c/
#
# Given: a list of k-mers.
# Return: the overlap graph (adjacency list): for each k-mer a, list all k-mers b
# such that Suffix(a) = Prefix(b), i.e., a[1:] == b[:-1].

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3c.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]
    # Index k-mers by their prefix (all but last char)
    by_prefix = defaultdict(list)
    for kmer in kmers:
        by_prefix[kmer[:-1]].append(kmer)

    adj = defaultdict(list)
    for kmer in kmers:
        suffix = kmer[1:]   # overlap: suffix of kmer = prefix of neighbour
        for neighbour in by_prefix[suffix]:
            adj[kmer].append(neighbour)

    for kmer in sorted(adj):
        print(f"{kmer} -> {','.join(sorted(adj[kmer]))}")

if __name__ == '__main__': solve(get_input())
