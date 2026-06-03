# BA1D — Find All Occurrences of a Pattern in a String
# https://rosalind.info/problems/ba1d/
#
# Given: a DNA string Pattern and a genome Text.
# Return: all starting positions (0-indexed) where Pattern appears in Text.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba1d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    pattern, text = lines[0].strip(), lines[1].strip()
    m = len(pattern)
    positions = [i for i in range(len(text) - m + 1) if text[i:i+m] == pattern]
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
