# BA3C — Construct the Overlap Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3c/
#
# Given: a list of k-mers.
# Return: the overlap graph (adjacency list): for each k-mer a, list all k-mers b
# such that Suffix(a) = Prefix(b), i.e., a[1:] == b[:-1].

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3c.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]
    # Index k-mers by their prefix (all but last char)
    by_prefix = defaultdict(list)
    for kmer in kmers:
        by_prefix[kmer[:-1]].append(kmer)

    adj = defaultdict(list)
    for kmer in kmers:
        suffix = kmer[1:]   # overlap: suffix of kmer = prefix of neighbour
        for neighbour in by_prefix[suffix]:
            adj[kmer].append(neighbour)

    for kmer in sorted(adj):
        print(f"{kmer} -> {','.join(sorted(adj[kmer]))}")

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
