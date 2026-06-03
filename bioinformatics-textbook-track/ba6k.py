# BA6K — Implement 2-BreakOnGenome
# https://rosalind.info/problems/ba6k/
#
# Given: A genome P and four distinct indices i1, i2, i3, i4.
# Return: The genome resulting from applying 2-BreakOnGenome(P, i1, i2, i3, i4).
#
# 2-BreakOnGenome converts the genome to its colored-edge graph, applies the
# 2-break (removing edges (i1,i2) and (i3,i4), adding (i1,i3) and (i2,i4)),
# then converts back to a genome.

import os, sys, re
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6k.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def chromosome_to_cycle(chrom):
    nodes = []
    for x in chrom:
        if x > 0: nodes.extend([2*x - 1, 2*x])
        else:     nodes.extend([-2*x, -2*x - 1])
    return nodes

def cycle_to_chromosome(cycle):
    chrom = []
    for i in range(0, len(cycle), 2):
        t, h = cycle[i], cycle[i+1]
        if h == t + 1: chrom.append(h // 2)
        else:          chrom.append(-(t // 2))
    return chrom

def colored_edges(genome):
    edges = set()
    for chrom in genome:
        nodes = chromosome_to_cycle(chrom)
        n = len(nodes)
        for i in range(1, n, 2):
            u, v = nodes[i], nodes[(i+1) % n]
            edges.add((u, v))
    return edges

def graph_to_genome(edges):
    adj = defaultdict(int)
    for u, v in edges:
        adj[u] = v
        adj[v] = u
    visited = set()
    chromosomes = []
    all_nodes = set(adj.keys())
    while all_nodes - visited:
        start = min(all_nodes - visited)
        cycle = []
        node = start
        while True:
            cycle.append(node)
            visited.add(node)
            # Black edge: head ↔ tail of the same synteny block
            nxt = node + 1 if node % 2 == 1 else node - 1
            cycle.append(nxt)
            visited.add(nxt)
            node = adj[nxt]
            if node == start: break
        chromosomes.append(cycle_to_chromosome(cycle))
    return chromosomes

def parse_genome(s):
    chromosomes = []
    for chrom_str in re.findall(r'\(([^)]+)\)', s):
        chrom = list(map(int, chrom_str.split()))
        chromosomes.append(chrom)
    return chromosomes

def format_genome(genome):
    parts = []
    for chrom in genome:
        tokens = [('+' + str(b) if b > 0 else str(b)) for b in chrom]
        parts.append('(' + ' '.join(tokens) + ')')
    return ' '.join(parts)

def two_break_on_genome(genome, i1, i2, i3, i4):
    edges = colored_edges(genome)
    # Remove edges (i1,i2) and (i3,i4); add (i1,i3) and (i2,i4)
    edges.discard((i1, i2)); edges.discard((i2, i1))
    edges.discard((i3, i4)); edges.discard((i4, i3))
    edges.add((i1, i3))
    edges.add((i2, i4))
    return graph_to_genome(edges)

def solve(data):
    lines = data.splitlines()
    genome = parse_genome(lines[0])
    i1, i2, i3, i4 = map(int, lines[1].split(','))
    result = two_break_on_genome(genome, i1, i2, i3, i4)
    print(format_genome(result))

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
