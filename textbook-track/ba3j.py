# BA3J — Reconstruct a String from its Paired Composition
# https://rosalind.info/problems/ba3j/
#
# Given: integers k and d, and a list of (k,d)-mers (paired reads).
# Return: a string reconstructed using the paired De Bruijn graph.
#
# A (k,d)-mer (a|b) represents a pair of k-mers with a gap of d between them.
# Build a De Bruijn graph where edges correspond to (k,d)-mers and nodes to
# paired (k-1)-mers, then find an Eulerian path.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3j.txt')
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
    k, d = map(int, lines[0].split())
    pairs = [l.strip().split('|') for l in lines[1:] if l.strip()]

    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    nodes = set()
    for a, b in pairs:
        u = (a[:-1], b[:-1])
        v = (a[1:], b[1:])
        graph[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1
        nodes.update([u, v])

    # Find Eulerian path
    start = end = None
    for node in nodes:
        diff = out_deg[node] - in_deg[node]
        if diff == 1:
            start = node
        elif diff == -1:
            end = node

    if start is None:
        path = eulerian_cycle(graph)
    else:
        graph[end].append(start)
        cycle = eulerian_cycle(graph)
        for i in range(len(cycle) - 1):
            if cycle[i] == end and cycle[i+1] == start:
                path = cycle[i+1:] + cycle[1:i+1]
                break

    # Reconstruct genome from path: prefix strand + suffix strand
    prefix_str = path[0][0] + ''.join(node[0][-1] for node in path[1:])
    suffix_str = path[0][1] + ''.join(node[1][-1] for node in path[1:])
    # Verify consistency: prefix_str[k+d:] should equal suffix_str[:-k-d]
    print(prefix_str)

if __name__ == '__main__': solve(get_input())
