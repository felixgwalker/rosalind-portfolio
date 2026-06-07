# Genome Assembly as Shortest Superstring (LONG)
# Rosalind problem: https://rosalind.info/problems/long/
#
# Problem: Given at most 50 DNA reads (each ≤ 1000 nt) where every read appears
# as a substring of some circular superstring, and the overlap between
# consecutive reads is more than half the read length (guaranteed unique
# assembly), find the shortest superstring.
#
# Algorithm: Greedy assembly.
#   1. Build an n×n overlap table: overlap[i][j] = length of longest suffix of
#      read[i] that is a prefix of read[j].
#   2. Repeatedly merge the pair with maximum overlap until one string remains.
#      (The Rosalind guarantee means greedy is optimal here.)
#
# Time: O(n²·L) for overlap computation, O(n³) total worst case.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_long.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read(), None

def parse_fasta(text):
    seqs = []
    parts = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if parts:
                seqs.append(''.join(parts))
            parts = []
        else:
            parts.append(line)
    if parts:
        seqs.append(''.join(parts))
    return seqs

def overlap(a, b):
    """Length of longest suffix of a that is a proper prefix of b."""
    max_ov = min(len(a), len(b))
    for length in range(max_ov, 0, -1):
        if a.endswith(b[:length]):
            return length
    return 0

def solve(data):
    reads = parse_fasta(data)

    # Remove reads that are substrings of other reads
    reads = [r for r in reads if not any(r in other for other in reads if r != other)]

    while len(reads) > 1:
        best_i, best_j, best_ov = 0, 1, -1
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i == j:
                    continue
                ov = overlap(reads[i], reads[j])
                if ov > best_ov:
                    best_ov = ov
                    best_i, best_j = i, j

        # Merge reads[best_i] with reads[best_j] using the overlap
        merged = reads[best_i] + reads[best_j][best_ov:]
        new_reads = [merged]
        for k in range(len(reads)):
            if k != best_i and k != best_j:
                new_reads.append(reads[k])
        reads = new_reads

    print(reads[0])

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
