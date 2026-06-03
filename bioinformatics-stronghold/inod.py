# Counting Phylogenetic Ancestors (INOD)
# Rosalind problem: https://rosalind.info/problems/inod/
#
# Problem: Given a positive integer n (≥ 3) representing the number of leaves
# in an unrooted binary tree, return the number of internal nodes.
#
# Combinatorial fact:
#   An unrooted binary tree with n leaves has exactly n - 2 internal nodes.
# Proof sketch: Each internal node has degree 3. A tree with n leaves and
# k internal nodes has n + k nodes and n + k - 1 edges. Counting edges via
# degree sum: 2(n + k - 1) = n·1 + k·3 → k = n - 2.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_inod.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    n = int(data.strip())
    print(n - 2)   # number of internal nodes in an unrooted binary tree with n leaves

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
