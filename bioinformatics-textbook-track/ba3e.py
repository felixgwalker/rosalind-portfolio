# BA3E — Construct the De Bruijn Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3e/
#
# Given: a list of k-mers.
# Return: the De Bruijn graph adjacency list: for each k-mer, add edge prefix → suffix.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3e.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]
    adj = defaultdict(list)
    for kmer in kmers:
        adj[kmer[:-1]].append(kmer[1:])
    for node in sorted(adj):
        print(f"{node} -> {','.join(adj[node])}")

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
