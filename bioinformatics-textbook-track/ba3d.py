# BA3D — Construct the De Bruijn Graph of a String
# https://rosalind.info/problems/ba3d/
#
# Given: an integer k and a DNA string Text.
# Return: the adjacency list of the De Bruijn graph Debruijn_k(Text).
# For each k-mer in Text, add an edge from its (k-1)-prefix to its (k-1)-suffix.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    k, text = int(lines[0].strip()), lines[1].strip()
    adj = defaultdict(set)
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        adj[kmer[:-1]].add(kmer[1:])
    for node in sorted(adj):
        print(f"{node} -> {','.join(sorted(adj[node]))}")

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
