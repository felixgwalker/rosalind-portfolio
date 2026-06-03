# Counting Subsets (SSET)
# Rosalind problem: https://rosalind.info/problems/sset/
#
# Problem: Given a positive integer n (≤ 1000), return the total number of
# subsets of a set of n elements modulo 1,000,000.
#
# The number of subsets of an n-element set (including the empty set) = 2^n.
# Python's pow(base, exp, mod) computes modular exponentiation efficiently.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_sset.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MOD = 1_000_000

def solve(data):
    n = int(data.strip())
    # pow(2, n, MOD) uses fast modular exponentiation — O(log n)
    print(pow(2, n, MOD))

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
