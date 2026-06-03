# BA6B — Compute the Number of Breakpoints in a Permutation
# https://rosalind.info/problems/ba6b/
#
# Given: a signed permutation P.
# Return: the number of breakpoints (adjacent pairs that are NOT consecutive).
# Prepend 0 and append n+1 to define extended permutation.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6b.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    perm = list(map(int, data.strip().strip('()').split()))
    extended = [0] + perm + [len(perm)+1]
    breakpoints = sum(1 for i in range(len(extended)-1) if extended[i+1] - extended[i] != 1)
    print(breakpoints)

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
