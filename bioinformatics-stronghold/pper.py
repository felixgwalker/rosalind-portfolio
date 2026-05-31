# Partial Permutations (PPER)
# Rosalind problem: https://rosalind.info/problems/pper/
#
# Problem: Given positive integers n and k (n ≤ 100, k ≤ n), return the number
# of partial permutations P(n, k) = n! / (n-k)! modulo 1,000,000.
# P(n, k) counts the number of ways to arrange k distinct objects chosen from n.
#
# Algorithm: Compute the falling factorial n × (n-1) × ... × (n-k+1) iteratively.
# Taking mod at each step keeps numbers small.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_pper.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

MOD = 1_000_000

def solve(data):
    n, k = map(int, data.split())
    result = 1
    # P(n,k) = n * (n-1) * ... * (n-k+1)  [k terms]
    for i in range(n, n - k, -1):
        result = (result * i) % MOD
    print(result)

if __name__ == '__main__':
    solve(get_input())
