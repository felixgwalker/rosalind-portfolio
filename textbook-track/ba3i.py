# BA3I — Find a k-Universal Circular String
# https://rosalind.info/problems/ba3i/
#
# Given: an integer k.
# Return: a k-universal circular binary string — a circular string of length 2^k
# that contains every binary k-mer exactly once.
#
# Algorithm: Find an Eulerian circuit in the De Bruijn graph of all binary (k-1)-mers.
# The circuit spells out the universal circular string.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3i.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def eulerian_cycle(graph):
    start = next(iter(graph))
    stack, circuit = [start], []
    while stack:
        v = stack[-1]
        if graph.get(v):
            stack.append(graph[v].pop())
        else:
            circuit.append(stack.pop())
    return circuit[::-1]

def solve(data):
    k = int(data.strip())
    # Generate all binary k-mers and build De Bruijn graph
    graph = defaultdict(list)
    for i in range(2 ** k):
        kmer = format(i, f'0{k}b')
        graph[kmer[:-1]].append(kmer[1:])
    cycle = eulerian_cycle(graph)
    # Reconstruct the circular string (length 2^k)
    result = cycle[0] + ''.join(n[-1] for n in cycle[1:-1])
    print(result)

if __name__ == '__main__': solve(get_input())
