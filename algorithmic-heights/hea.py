# Building a Heap (HEA)
# Rosalind problem: https://rosalind.info/problems/hea/
#
# Problem: Given an array of n integers, convert it into a max-heap using
# the standard bottom-up heapify algorithm and output the resulting array.
#
# Algorithm: Start from the last internal node (index n//2-1) and sift down
# each node towards the leaves. This builds a heap in O(n) time.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_hea.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def sift_down(arr, i, n):
    """Sift element at index i down to restore max-heap property in arr[0..n-1]."""
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

def build_heap(arr):
    n = len(arr)
    # Heapify from last internal node up to root
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)
    return arr

def solve(data):
    lines = data.splitlines()
    arr = list(map(int, lines[1].split()))
    print(' '.join(map(str, build_heap(arr))))

if __name__ == '__main__':
    solve(get_input())
