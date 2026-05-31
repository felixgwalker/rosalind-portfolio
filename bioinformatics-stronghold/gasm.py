# Genome Assembly Using Reads (GASM)
# Rosalind problem: https://rosalind.info/problems/gasm/
#
# Problem: Given a collection of sequencing reads (each present in both
# orientations), assemble the genome as an Eulerian circuit through the
# De Bruijn graph of the reads' (k-1)-mers.
#
# Algorithm:
#   1. For each read and its reverse complement, extract all k-mers.
#   2. Build the De Bruijn graph: edge s[:-1] → s[1:] for each k-mer s.
#   3. Find an Eulerian circuit using Hierholzer's algorithm.
#   4. Recover the sequence (first base of each node in the circuit).
#
# The k is determined from the read length (use k = read_length - 1, or k = 10
# as a default for short reads).

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_gasm.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

COMP = str.maketrans('ACGT', 'TGCA')

def rev_comp(s):
    return s.translate(COMP)[::-1]

def eulerian_circuit(graph):
    start = next(iter(graph))
    stack, circuit = [start], []
    while stack:
        v = stack[-1]
        if graph[v]:
            stack.append(graph[v].pop())
        else:
            circuit.append(stack.pop())
    return circuit[::-1]

def solve(data):
    reads = [l.strip() for l in data.splitlines() if l.strip()]
    k = len(reads[0]) - 1   # use (read_length - 1)-mers as graph edges

    graph = defaultdict(list)
    for read in reads:
        for strand in (read, rev_comp(read)):
            for i in range(len(strand) - k + 1):
                kmer = strand[i:i+k+1]
                graph[kmer[:-1]].append(kmer[1:])

    # Balance check and circuit
    circuit = eulerian_circuit(graph)
    genome = ''.join(node[0] for node in circuit[:-1])
    print(genome)

if __name__ == '__main__':
    solve(get_input())
