# Counting Unrooted Binary Trees (CUNR)
# Rosalind problem: https://rosalind.info/problems/cunr/
#
# Problem: Given a positive integer n, count the number of distinct unrooted
# binary trees with n labeled leaves (every internal node has degree 3).
#
# Formula: T(n) = (2n-5)!! = 1 × 3 × 5 × ... × (2n-5)  for n ≥ 3
#          T(1) = T(2) = T(3) = 1
# Each new leaf is inserted on one of the (2k-3) existing edges of a (k-leaf) tree.
#
# Return the answer modulo 1,000,000.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_cunr.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    n = int(data.strip())
    result = 1
    # Multiply by (2i-5) for i = 3..n; this gives 1*3*5*...*(2n-5)
    for i in range(3, n + 1):
        result = (result * (2 * i - 5)) % 1_000_000
    print(result)

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
