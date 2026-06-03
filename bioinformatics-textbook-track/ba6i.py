# BA6I — Implement GraphToGenome
# https://rosalind.info/problems/ba6i/
#
# Given: a list of colored edges.
# Return: the corresponding genome (multi-chromosomal signed permutation).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6i.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        t, h = cycle[i], cycle[i+1]
        if h == t + 1: chromosome.append(h // 2)
        else: chromosome.append(-(t // 2))
    return chromosome

def solve(data):
    adj = defaultdict(int)
    for line in data.splitlines():
        line = line.strip().strip('()')
        if not line: continue
        u, v = map(int, line.split(','))
        adj[u] = v; adj[v] = u

    visited = set()
    chromosomes = []
    # Build cycles: for each node, alternate between "black" edges (+1/-1) and colored edges
    all_nodes = set(adj.keys())
    while all_nodes - visited:
        start = min(all_nodes - visited)
        cycle = []
        node = start
        while True:
            cycle.append(node)
            visited.add(node)
            # Black edge: if node is even, next = node-1; if odd, next = node+1
            if node % 2 == 1: next_node = node + 1
            else: next_node = node - 1
            cycle.append(next_node)
            visited.add(next_node)
            # Colored edge
            node = adj[next_node]
            if node == start:
                break
        chromosomes.append(cycle_to_chromosome(cycle))

    result = ' '.join('(' + ' '.join(map(str, ch)) + ')' for ch in chromosomes)
    print(result)

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
