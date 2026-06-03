# 2-Way Partition (PAR)
# Rosalind problem: https://rosalind.info/problems/par/
#
# Problem: Given an array of n integers, partition it around the last element
# (pivot) such that all elements ≤ pivot come before it and all elements > pivot
# come after it. Output the resulting array after one partitioning step.
#
# This is the core of the Quicksort algorithm. The partition runs in O(n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_par.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def partition(arr):
    """In-place Lomuto partition using last element as pivot. Returns the array."""
    pivot = arr[-1]
    i = 0   # boundary: arr[0..i-1] are <= pivot
    for j in range(len(arr) - 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[-1] = arr[-1], arr[i]   # place pivot in its final position
    return arr

def solve(data):
    lines = data.splitlines()
    arr = list(map(int, lines[1].split()))
    print(' '.join(map(str, partition(arr))))

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
