# Weighted Median (MED)
# Rosalind problem: https://rosalind.info/problems/med/
#
# Problem: Given a list of values and their positive weights, find the weighted
# median — the smallest value m such that the sum of weights of values ≤ m
# is at least 1/2 the total weight, AND the sum of weights of values ≥ m is
# at least 1/2 the total weight.
#
# Algorithm: Sort by value, accumulate weights, find the crossing point. O(n log n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_med.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n = int(lines[0])
    values = list(map(float, lines[1].split()))
    weights = list(map(float, lines[2].split()))

    # Sort by value
    pairs = sorted(zip(values, weights))
    total = sum(weights)
    half = total / 2

    cumsum = 0
    for val, w in pairs:
        cumsum += w
        if cumsum >= half:
            print(val)
            return

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
