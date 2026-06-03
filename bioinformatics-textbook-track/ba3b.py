# BA3B — Reconstruct a String from its Genome Path
# https://rosalind.info/problems/ba3b/
#
# Given: a list of k-mers forming a genome path (each adjacent pair overlaps by k-1).
# Return: the string that spells this genome path.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3b.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    kmers = [l.strip() for l in data.splitlines() if l.strip()]
    genome = kmers[0]
    for kmer in kmers[1:]:
        genome += kmer[-1]   # each consecutive k-mer adds one new character
    print(genome)

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
