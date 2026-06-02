# BA3H — Reconstruct a String from its k-mer Composition
# https://rosalind.info/problems/ba3h/
#
# Given: an integer k and a list of k-mers.
# Return: the string reconstructed from this composition using the Eulerian path
# through the De Bruijn graph.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3h.txt')
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
    lines = data.splitlines()
    k = int(lines[0].strip())
    kmers = [l.strip() for l in lines[1:] if l.strip()]

    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    nodes = set()
    for kmer in kmers:
        u, v = kmer[:-1], kmer[1:]
        graph[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1
        nodes.update([u, v])

    # Find start and end for Eulerian path
    start = end = None
    for node in nodes:
        diff = out_deg[node] - in_deg[node]
        if diff == 1:
            start = node
        elif diff == -1:
            end = node

    if start is None:   # Eulerian cycle
        cycle = eulerian_cycle(graph)
        print(cycle[0] + ''.join(n[-1] for n in cycle[1:-1]))
        return

    # Add virtual edge, find cycle, rotate
    graph[end].append(start)
    cycle = eulerian_cycle(graph)
    for i in range(len(cycle) - 1):
        if cycle[i] == end and cycle[i+1] == start:
            path = cycle[i+1:] + cycle[1:i+1]
            print(path[0] + ''.join(n[-1] for n in path[1:]))
            return

if __name__ == '__main__': solve(get_input())
