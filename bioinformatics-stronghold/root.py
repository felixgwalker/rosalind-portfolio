# Counting Rooted Binary Trees (ROOT)
# Rosalind problem: https://rosalind.info/problems/root/
#
# Problem: Given a positive integer n, count the number of distinct rooted
# binary trees with n labeled leaves (root and every internal node has
# exactly 2 children).
#
# Formula: T(n) = (2n-3)!! = 1 × 3 × 5 × ... × (2n-3)  for n ≥ 2
#          T(1) = 1
# Equivalently, an unrooted binary tree on n leaves can be rooted on any
# of its (2n-3) edges, giving T(n) = T_unrooted(n) × (2n-3).
#
# Return the answer modulo 1,000,000.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_root.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    n = int(data.strip())
    result = 1
    # Multiply by (2i-3) for i = 2..n; this gives 1*3*5*...*(2n-3)
    for i in range(2, n + 1):
        result = (result * (2 * i - 3)) % 1_000_000
    print(result)

if __name__ == '__main__':
    solve(get_input())
