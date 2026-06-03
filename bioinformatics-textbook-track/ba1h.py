# BA1H — Find All Approximate Occurrences of a Pattern in a String
# https://rosalind.info/problems/ba1h/
#
# Given: strings Pattern and Text, and integer d.
# Return: all positions where Pattern occurs in Text with at most d mismatches.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba1h.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def solve(data):
    lines = data.splitlines()
    pattern, text, d = lines[0].strip(), lines[1].strip(), int(lines[2].strip())
    m = len(pattern)
    positions = [i for i in range(len(text) - m + 1) if hamming(text[i:i+m], pattern) <= d]
    print(' '.join(map(str, positions)))

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
