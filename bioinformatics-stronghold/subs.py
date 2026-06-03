# Finding a Motif in DNA (SUBS)
# Rosalind problem: https://rosalind.info/problems/subs/
#
# Problem: Given a DNA string s and a shorter pattern t, return all 1-indexed
# starting positions where t appears as a (possibly overlapping) substring of s.
#
# Algorithm: Naive sliding-window — check every window of width len(t).
# O(n·m) in the worst case, but fast in practice for Rosalind's input sizes.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_subs.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    s, t = lines[0].strip(), lines[1].strip()
    m = len(t)
    positions = []
    for i in range(len(s) - m + 1):
        if s[i:i+m] == t:
            positions.append(i + 1)    # +1 for 1-based indexing
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
