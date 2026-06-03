# 3-Sum Problem (3SUM)
# Rosalind problem: https://rosalind.info/problems/3sum/
#
# Problem: Given k arrays each of n integers, find three distinct indices i, j, k
# such that A[i] + A[j] + A[k] = 0. Output the 1-based indices or -1 -1 -1 if
# no such triple exists.
#
# Algorithm: Sort + two-pointer sweep — O(n²) per array.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_3sum.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def three_sum(arr):
    """Find 1-based indices (i,j,k) with arr[i-1]+arr[j-1]+arr[k-1]==0."""
    n = len(arr)
    indexed = sorted(enumerate(arr, 1), key=lambda x: x[1])
    for a in range(n):
        idx_a, val_a = indexed[a]
        lo, hi = a + 1, n - 1
        while lo < hi:
            s = val_a + indexed[lo][1] + indexed[hi][1]
            if s == 0:
                idxs = sorted([idx_a, indexed[lo][0], indexed[hi][0]])
                return idxs
            elif s < 0:
                lo += 1
            else:
                hi -= 1
    return [-1, -1, -1]

def solve(data):
    lines = data.splitlines()
    k, n = map(int, lines[0].split())
    for i in range(1, k + 1):
        arr = list(map(int, lines[i].split()))
        result = three_sum(arr)
        print(' '.join(map(str, result)))

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
