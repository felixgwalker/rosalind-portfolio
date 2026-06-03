# BA3K — Generate Contigs from a Collection of Reads
# https://rosalind.info/problems/ba3k/
#
# Given: a list of k-mers.
# Return: all contigs — maximal paths in the De Bruijn graph that are not
# branching (i.e., the internal nodes all have in-degree = out-degree = 1).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3k.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]
    adj = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    nodes = set()
    for kmer in kmers:
        u, v = kmer[:-1], kmer[1:]
        adj[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1
        nodes.update([u, v])

    # A non-branching path starts at a node where in-deg != 1 or out-deg != 1
    # and extends through nodes with in-deg == out-deg == 1
    visited_edges = defaultdict(int)   # track which edges have been used
    contigs = []

    def maximal_nonbranching_path(start, first_neighbour):
        path = [start, first_neighbour]
        visited_edges[(start, first_neighbour)] += 1
        v = first_neighbour
        while in_deg[v] == 1 and out_deg[v] == 1:
            w = adj[v][0]
            visited_edges[(v, w)] += 1
            path.append(w)
            v = w
        return path

    for v in sorted(nodes):
        if not (in_deg[v] == 1 and out_deg[v] == 1):
            if out_deg[v] > 0:
                for w in adj[v]:
                    if visited_edges[(v, w)] == 0:
                        path = maximal_nonbranching_path(v, w)
                        contigs.append(path[0] + ''.join(n[-1] for n in path[1:]))

    # Handle isolated cycles (all nodes have in-deg == out-deg == 1)
    for v in sorted(nodes):
        if in_deg[v] == 1 and out_deg[v] == 1:
            if any(visited_edges[(v, w)] == 0 for w in adj[v]):
                w = adj[v][0]
                if visited_edges[(v, w)] == 0:
                    path = maximal_nonbranching_path(v, w)
                    contigs.append(path[0] + ''.join(n[-1] for n in path[1:]))

    print('\n'.join(contigs))

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
