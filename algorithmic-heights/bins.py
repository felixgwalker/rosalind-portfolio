# Binary Search (BINS)
# Rosalind problem: https://rosalind.info/problems/bins/
#
# Problem: Given a sorted array A and a list of keys, for each key return its
# 1-indexed position in A, or -1 if not found. Use binary search — O(log n) per query.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_bins.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def binary_search(A, key):
    """Return 1-indexed position of key in sorted array A, or -1."""
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] == key:
            return mid + 1   # 1-indexed
        elif A[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def solve(data):
    lines = data.splitlines()
    # n = len(array), k = number of queries
    n = int(lines[0])
    k = int(lines[1])
    A = list(map(int, lines[2].split()))
    keys = list(map(int, lines[3].split()))
    results = [binary_search(A, key) for key in keys]
    print(' '.join(map(str, results)))

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
