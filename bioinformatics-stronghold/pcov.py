# Genome Assembly with Perfect Coverage (PCOV)
# Rosalind problem: https://rosalind.info/problems/pcov/
#
# Problem: Given a collection of (k)-mers with perfect circular coverage
# (every (k-1)-mer of the genome appears exactly once as a prefix AND once as
# a suffix among the k-mers), reconstruct the circular genome using an
# Eulerian circuit through the De Bruijn graph.
#
# Algorithm:
#   1. Build De Bruijn graph: each k-mer s gives edge s[:-1] → s[1:].
#   2. Find an Eulerian circuit (each node has equal in/out degree by construction).
#   3. Recover the sequence from the circuit (first char of each node in the path).

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_pcov.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def eulerian_circuit(graph):
    """Hierholzer's algorithm for Eulerian circuit in a directed graph.
    graph: dict of node -> list of neighbours (mutable — consumed during traversal)."""
    # Start from any node
    start = next(iter(graph))
    stack = [start]
    circuit = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            stack.append(u)
        else:
            circuit.append(stack.pop())
    return circuit[::-1]

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]

    # Build adjacency list of the De Bruijn graph
    graph = defaultdict(list)
    for kmer in kmers:
        graph[kmer[:-1]].append(kmer[1:])

    circuit = eulerian_circuit(graph)
    # The circular genome is the first character of each node in the circuit
    # (skip the last node since it wraps around to the first)
    genome = ''.join(node[0] for node in circuit[:-1])
    print(genome)

if __name__ == '__main__':
    solve(get_input())
