# BA2B — Find a Median String
# https://rosalind.info/problems/ba2b/
#
# Given: integer k and a list of DNA strings.
# Return: a k-mer Pattern that minimises d(Pattern, Dna) = sum of minimum
# Hamming distances from Pattern to each string in Dna.
#
# Algorithm: Enumerate all 4^k possible k-mers; for each compute the total
# distance to all strings and take the minimum. O(4^k * n * L * k).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba2b.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def distance_to_strings(pattern, dna):
    k = len(pattern)
    return sum(min(hamming(pattern, s[i:i+k]) for i in range(len(s)-k+1)) for s in dna)

def all_kmers(k, alpha='ACGT'):
    if k == 0:
        yield ''; return
    for c in alpha:
        for rest in all_kmers(k - 1, alpha):
            yield c + rest

def solve(data):
    lines = data.splitlines()
    k = int(lines[0].strip())
    dna = [l.strip() for l in lines[1:] if l.strip()]
    best_pattern, best_dist = None, float('inf')
    for pattern in all_kmers(k):
        d = distance_to_strings(pattern, dna)
        if d < best_dist:
            best_dist = d
            best_pattern = pattern
    print(best_pattern)

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
