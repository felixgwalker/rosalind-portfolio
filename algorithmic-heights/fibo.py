# Fibonacci Numbers (FIBO)
# Rosalind problem: https://rosalind.info/problems/fibo/
#
# Problem: Given n, compute the n-th Fibonacci number.
# F(1) = F(2) = 1; F(n) = F(n-1) + F(n-2) for n > 2.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_fibo.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

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
