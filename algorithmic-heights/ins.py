# Insertion Sort (INS)
# Rosalind problem: https://rosalind.info/problems/ins/
#
# Problem: Given an array of n integers, count the number of swaps required
# by insertion sort to sort it. (Each swap moves an element one position left.)
# This count equals the number of inversions in the array.
#
# Algorithm: Count inversions using merge sort — O(n log n). Each inversion
# (pair i < j where A[i] > A[j]) corresponds to exactly one swap in insertion sort.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_ins.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def count_inversions(arr):
    """Count inversions using merge sort. Returns (sorted_arr, inversion_count)."""
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, lc = count_inversions(arr[:mid])
    right, rc = count_inversions(arr[mid:])
    merged = []
    count = lc + rc
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            count += len(left) - i   # all remaining left elements are inversions
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count

def solve(data):
    lines = data.splitlines()
    arr = list(map(int, lines[1].split()))
    _, inversions = count_inversions(arr)
    print(inversions)

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
