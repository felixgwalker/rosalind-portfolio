# BA9I — Construct the Burrows-Wheeler Transform of a String
# https://rosalind.info/problems/ba9i/
#
# Given: a DNA string s. Return: the BWT of s (last column of the cyclic rotation matrix).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9i.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def bwt(s):
    rotations = sorted(s[i:] + s[:i] for i in range(len(s)))
    return ''.join(r[-1] for r in rotations)

def solve(data):
    print(bwt(data.strip()))

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
