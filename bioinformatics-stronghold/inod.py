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
                        '..', 'rosalind-files', 'rosalind_inod.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    n = int(data.strip())
    print(n - 2)   # number of internal nodes in an unrooted binary tree with n leaves

if __name__ == '__main__':
    solve(get_input())
