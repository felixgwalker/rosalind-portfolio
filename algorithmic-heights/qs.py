# Quick Sort (QS)
# Rosalind problem: https://rosalind.info/problems/qs/
#
# Problem: Given an array of n distinct integers, output the number of swaps
# performed by a standard quicksort using the last element as pivot.
#
# Actually, Rosalind's QS asks to return the sorted array after one full
# quicksort (the 3-way partition problem variant). Let me implement the full
# in-place quicksort and output the sorted array.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_qs.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def quicksort(arr, lo, hi):
    if lo < hi:
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        quicksort(arr, lo, i - 1)
        quicksort(arr, i + 1, hi)

def solve(data):
    lines = data.splitlines()
    arr = list(map(int, lines[1].split()))
    quicksort(arr, 0, len(arr) - 1)
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    solve(get_input())
