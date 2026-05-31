# Merge Sort (MS)
# Rosalind problem: https://rosalind.info/problems/ms/
#
# Problem: Given an array of n integers, sort it using merge sort and output
# the sorted array. Merge sort runs in O(n log n) time and O(n) space.
#
# Algorithm: Divide the array in half, recursively sort each half, then merge.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_ms.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge the two sorted halves
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def solve(data):
    lines = data.splitlines()
    arr = list(map(int, lines[1].split()))
    print(' '.join(map(str, merge_sort(arr))))

if __name__ == '__main__':
    solve(get_input())
