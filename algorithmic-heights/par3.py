# 3-Way Partition (PAR3)
# Rosalind problem: https://rosalind.info/problems/par3/
#
# Problem: Given an array of n integers, perform a 3-way partition using the
# last element as pivot: rearrange so all elements < pivot come first, then
# elements == pivot, then elements > pivot. Output the resulting array.
#
# Also known as the Dutch National Flag algorithm — O(n) time.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_par3.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def partition3(arr):
    """Dutch National Flag partition: [<pivot] [==pivot] [>pivot]."""
    pivot = arr[-1]
    lo = 0        # boundary: all arr[0..lo-1] < pivot
    mid = 0       # boundary: all arr[lo..mid-1] == pivot
    hi = len(arr) - 1   # boundary: all arr[hi+1..] > pivot

    while mid <= hi:
        if arr[mid] < pivot:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1

    return arr

def solve(data):
    lines = data.splitlines()
    arr = list(map(int, lines[1].split()))
    print(' '.join(map(str, partition3(arr))))

if __name__ == '__main__':
    solve(get_input())
