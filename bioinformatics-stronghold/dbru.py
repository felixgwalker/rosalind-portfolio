# Constructing a De Bruijn Graph (DBRU)
# Rosalind problem: https://rosalind.info/problems/dbru/
#
# Problem: Given a collection of DNA strings of equal length k, construct the
# De Bruijn graph where:
#   - Each string s contributes an edge from s[:-1] to s[1:]
#   - Also include the reverse complement of each string
#   - Output unique directed edges as "(prefix, suffix)" pairs, sorted.
#
# The De Bruijn graph is the foundation of sequence assembly: reads become edges,
# and assembly is an Eulerian path through the graph.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_dbru.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

COMP = str.maketrans('ACGT', 'TGCA')

def rev_comp(s):
    return s.translate(COMP)[::-1]

def solve(data):
    strings = [l.strip() for l in data.splitlines() if l.strip()]
    edges = set()
    for s in strings:
        edges.add((s[:-1], s[1:]))           # forward edge
        rc = rev_comp(s)
        edges.add((rc[:-1], rc[1:]))          # reverse complement edge
    for u, v in sorted(edges):
        print(f"({u}, {v})")

if __name__ == '__main__':
    solve(get_input())
