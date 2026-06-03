# BA6D — Find a Shortest Transformation of One Genome into Another by 2-Breaks
# https://rosalind.info/problems/ba6d/
#
# Apply 2-breaks until the genome P equals genome Q, minimising the number of steps.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_genome(s):
    chromosomes = []
    for block in s.strip().split(')('):
        block = block.strip('()')
        chromosomes.append(list(map(int, block.split())))
    return chromosomes

def chromosome_to_cycle(chrom):
    nodes = []
    for x in chrom:
        if x > 0: nodes.extend([2*x-1, 2*x])
        else: nodes.extend([-2*x, -2*x-1])
    return nodes

def colored_edges(genome):
    edges = {}
    for chrom in genome:
        nodes = chromosome_to_cycle(chrom)
        n = len(nodes)
        for i in range(1, n, 2):
            u, v = nodes[i], nodes[(i+1)%n]
            edges[u] = v; edges[v] = u
    return edges

def cycle_to_chromosome(cycle):
    chrom = []
    for i in range(0, len(cycle), 2):
        t, h = cycle[i], cycle[i+1]
        if h == t+1: chrom.append(h//2)
        else: chrom.append(-(t//2))
    return chrom

def graph_to_genome(P_edges, n_blocks):
    visited = set()
    chromosomes = []
    for start in range(1, 2*n_blocks+1):
        if start in visited: continue
        cycle = []; node = start
        while True:
            cycle.append(node); visited.add(node)
            if node % 2 == 1: nxt = node+1
            else: nxt = node-1
            cycle.append(nxt); visited.add(nxt)
            node = P_edges.get(nxt, -1)
            if node == start or node == -1: break
        if cycle: chromosomes.append(cycle_to_chromosome(cycle))
    return chromosomes

def fmt_genome(genome):
    return ' '.join('('+' '.join(map(str,ch))+')' for ch in genome)

def two_break_on_genome(P_edges, i1, i2, i3, i4):
    P_edges[i1] = i3; P_edges[i3] = i1
    P_edges[i2] = i4; P_edges[i4] = i2

def solve(data):
    lines = data.splitlines()
    P = parse_genome(lines[0]); Q = parse_genome(lines[1])
    n = sum(len(ch) for ch in P)
    P_edges = colored_edges(P)
    Q_edges = colored_edges(Q)

    print(fmt_genome(P))
    while True:
        # Find a non-trivial cycle in breakpoint graph
        adj = defaultdict(list)
        for u, v in P_edges.items(): adj[u].append((v,'P'))
        for u, v in Q_edges.items(): adj[u].append((v,'Q'))
        # Find a Q-edge in a cycle of length > 1 (a cycle with > 2 nodes)
        found = False
        for start in range(1, 2*n+1):
            # Try to find a cycle starting with a Q-edge that needs breaking
            q_end = Q_edges.get(start, -1)
            if q_end == -1: continue
            p_partner = P_edges.get(start, -1)
            if p_partner == q_end: continue  # already a trivial cycle
            # 2-break: (p_start, p_partner) and (q_start, q_end) → (p_start, q_end) and (p_partner, q_start)
            i1, i2 = start, P_edges[start]
            i3, i4 = Q_edges[start], Q_edges[P_edges[start]]
            two_break_on_genome(P_edges, i1, i2, i3, i4)
            P = graph_to_genome(P_edges, n)
            print(fmt_genome(P))
            found = True
            break
        if not found: break

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
