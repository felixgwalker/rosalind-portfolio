# Genome Assembly with Perfect Coverage Revisited (GREP)
# Rosalind problem: https://rosalind.info/problems/grep/
#
# Problem: Given a collection of DNA reads of equal length drawn from BOTH
# strands of a circular genome (i.e., the read set is closed under reverse
# complement), reconstruct the circular genome using a de Bruijn graph.
#
# Algorithm:
#   1. Deduplicate reads: keep only the lexicographically smaller of each
#      (read, rev_comp) pair, so each genomic position contributes one edge.
#   2. Build a de Bruijn graph: each k-mer read → directed edge from
#      prefix (k-1)-mer to suffix (k-1)-mer.
#   3. Find an Eulerian circuit (the graph is balanced by construction).
#   4. Read off the assembled circular sequence.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_grep.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def rev_comp(s):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[c] for c in reversed(s))

def eulerian_circuit(graph):
    """Hierholzer's algorithm on a dict {node: [neighbours]}."""
    start = next(iter(graph))
    stack = [start]
    circuit = []
    while stack:
        v = stack[-1]
        if graph[v]:
            stack.append(graph[v].pop())
        else:
            circuit.append(stack.pop())
    return circuit[::-1]

def solve(data):
    reads = [l.strip() for l in data.splitlines() if l.strip() and not l.startswith('>')]
    if not reads:
        return

    k = len(reads[0])

    # Keep only canonical (lexicographically smaller) orientation
    canonical = set()
    for r in reads:
        rc = rev_comp(r)
        canonical.add(min(r, rc))

    # Build de Bruijn graph
    graph = defaultdict(list)
    for r in canonical:
        u, v = r[:-1], r[1:]
        graph[u].append(v)
        # Reverse complement edge
        ru, rv = rev_comp(v), rev_comp(u)
        graph[ru].append(rv)

    circuit = eulerian_circuit(graph)
    # Circuit visits each node; concatenate first chars to get the genome
    genome = ''.join(node[0] for node in circuit[:-1])
    print(genome)

if __name__ == '__main__':
    solve(get_input())
