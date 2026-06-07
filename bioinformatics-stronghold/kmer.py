# k-Mer Composition (KMER)
# Rosalind problem: https://rosalind.info/problems/kmer/
#
# Problem: Given a DNA string s in FASTA format, return its 4-mer composition:
# the 4^4 = 256 frequencies of all 4-mers, listed in lexicographic order
# (AAAA, AAAC, AAAG, AAAT, AACA, ..., TTTT), space-separated.
#
# Algorithm: Sliding window of length 4 across the string; look up each k-mer
# in a pre-built index. O(n + 4^k).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_kmer.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read(), None

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        if not line.startswith('>'):
            parts.append(line.strip())
    return ''.join(parts)

def all_kmers(k, alphabet='ACGT'):
    """Generate all k-mers over alphabet in lexicographic order."""
    if k == 0:
        yield ''
        return
    for base in alphabet:
        for rest in all_kmers(k - 1, alphabet):
            yield base + rest

def solve(data):
    s = parse_fasta(data)
    k = 4
    # Build frequency dict; initialise all k-mers to 0
    freq = {km: 0 for km in all_kmers(k)}
    for i in range(len(s) - k + 1):
        kmer = s[i:i+k]
        if kmer in freq:
            freq[kmer] += 1
    # Output in lexicographic order
    print(' '.join(str(freq[km]) for km in sorted(freq)))

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
