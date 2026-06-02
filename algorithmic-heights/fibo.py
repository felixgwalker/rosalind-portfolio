# Fibonacci Numbers (FIBO)
# Rosalind problem: https://rosalind.info/problems/fibo/
#
# Problem: Given n, compute the n-th Fibonacci number.
# F(1) = F(2) = 1; F(n) = F(n-1) + F(n-2) for n > 2.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_fibo.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    n = int(data.strip())
    if n <= 2:
        print(1)
        return
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    print(b)

if __name__ == '__main__':
    solve(get_input())
