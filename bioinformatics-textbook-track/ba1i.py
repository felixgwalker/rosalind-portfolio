# BA1I — Find the Most Frequent Words with Mismatches in a String
# https://rosalind.info/problems/ba1i/
#
# Given: a string Text and integers k and d.
# Return: all k-mers Pattern maximising Count_d(Text, Pattern) — the number of
# approximate occurrences of Pattern in Text with at most d mismatches.
#
# Algorithm: For each window position in Text, enumerate all k-mers within
# Hamming distance d of the window and increment their counts. O(n * 4^d * k).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba1i.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def neighbors(pattern, d):
    """Generate all strings within Hamming distance d of pattern."""
    if d == 0:
        yield pattern
        return
    if len(pattern) == 0:
        yield ''
        return
    for rest in neighbors(pattern[1:], d):
        yield pattern[0] + rest
    if d > 0:
        for base in 'ACGT':
            if base != pattern[0]:
                for rest in neighbors(pattern[1:], d - 1):
                    yield base + rest

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip()
    k, d = map(int, lines[1].split())
    n = len(text)
    freq = defaultdict(int)
    for i in range(n - k + 1):
        window = text[i:i+k]
        for nb in neighbors(window, d):
            freq[nb] += 1
    max_count = max(freq.values())
    print(' '.join(kmer for kmer, c in freq.items() if c == max_count))

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
