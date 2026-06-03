# BA3A — Generate the k-mer Composition of a String
# https://rosalind.info/problems/ba3a/
#
# Given: an integer k and a DNA string Text.
# Return: the k-mer composition of Text: all k-mers in lexicographic order (with multiplicity).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba3a.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    k, text = int(lines[0].strip()), lines[1].strip()
    kmers = sorted(text[i:i+k] for i in range(len(text) - k + 1))
    print('\n'.join(kmers))

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
