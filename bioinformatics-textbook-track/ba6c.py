# BA6C — Compute the 2-Break Distance Between a Pair of Genomes
# https://rosalind.info/problems/ba6c/
#
# Given: two genomes (multi-chromosomal signed permutations).
# Return: the 2-break distance = n - cycles(P, Q), where n is the number of
# synteny blocks and cycles is the number of cycles in the "breakpoint graph".

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6c.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_genome(s):
    chromosomes = []
    for block in s.strip().split(')('):
        block = block.strip('()')
        chromosomes.append(list(map(int, block.split())))
    return chromosomes

def chromosome_to_cycle(chromosome):
    nodes = []
    for x in chromosome:
        if x > 0:
            nodes.extend([2*x-1, 2*x])
        else:
            nodes.extend([-2*x, -2*x-1])
    return nodes

def colored_edges(genome):
    edges = set()
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        n = len(nodes)
        for i in range(1, n, 2):
            edges.add((nodes[i], nodes[(i+1)%n]))
    return edges

def count_cycles(edges_P, edges_Q):
    # Build adjacency from union of both colored edge sets
    adj = defaultdict(list)
    for u, v in edges_P: adj[u].append(v); adj[v].append(u)
    for u, v in edges_Q: adj[u].append(v); adj[v].append(u)
    visited = set()
    cycles = 0
    for start in adj:
        if start not in visited:
            cycles += 1
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for nb in adj[node]:
                        if nb not in visited:
                            stack.append(nb)
    return cycles

def solve(data):
    lines = data.splitlines()
    P = parse_genome(lines[0])
    Q = parse_genome(lines[1])
    n = sum(len(ch) for ch in P)
    ep = colored_edges(P)
    eq = colored_edges(Q)
    cycles = count_cycles(ep, eq)
    print(n - cycles)

if __name__ == '__main__':
    import io, contextlib
    data, out_path = get_input()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        solve(data)
    output = buf.getvalue()
    sys.stdout.write(output)
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(output)
