# BA6H — Implement ColoredEdges
# https://rosalind.info/problems/ba6h/
#
# Given: a genome (multi-chromosomal signed permutation).
# Return: the colored edges of the genome's cycle graph.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6h.txt')
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
        if x > 0: nodes.extend([2*x-1, 2*x])
        else: nodes.extend([-2*x, -2*x-1])
    return nodes

def solve(data):
    genome = parse_genome(data.strip())
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        n = len(nodes)
        for i in range(1, n, 2):
            edges.append((nodes[i], nodes[(i+1) % n]))
    for e in edges:
        print(f"({e[0]}, {e[1]})")

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
