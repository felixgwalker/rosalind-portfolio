# Rabbits and Recurrence Relations (FIB)
# Rosalind problem: https://rosalind.info/problems/fib/
#
# Problem: Given n (months, ≤ 40) and k (offspring pairs per mating, ≤ 5),
# compute the number of rabbit pairs after n months.
# Each pair matures in one month and then produces k new pairs every month.
#
# Recurrence: F(1) = F(2) = 1;  F(n) = F(n-1) + k * F(n-2)
# This is a generalised Fibonacci sequence. Standard Fibonacci has k = 1.
# We use iterative DP to avoid exponential recursion. O(n) time, O(1) space.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_fib.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    n, k = map(int, data.split())

    # Base cases: 1 pair in month 1 and month 2
    prev, curr = 1, 1

    for _ in range(2, n):
        # New pairs this month = all current adults breed (curr) plus
        # every pair that was young last month is now adult (k * prev offspring each)
        prev, curr = curr, curr + k * prev

    print(curr)

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
