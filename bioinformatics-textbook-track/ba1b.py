# BA1B — Find the Most Frequent k-mers in a String
# https://rosalind.info/problems/ba1b/
#
# Given: a DNA string Text and integer k.
# Return: all k-mers that appear most frequently (max count) in Text.

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba1b.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    text, k = lines[0].strip(), int(lines[1].strip())
    freq = Counter(text[i:i+k] for i in range(len(text) - k + 1))
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
