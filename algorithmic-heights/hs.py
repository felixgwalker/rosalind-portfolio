# Heap Sort (HS)
# Rosalind problem: https://rosalind.info/problems/hs/
#
# Problem: Given an array, sort it using heap sort and output the sorted array.
# Heap sort has O(n log n) time and O(1) extra space.
#
# Algorithm:
#   1. Build a max-heap from the array (heapify in O(n)).
#   2. Repeatedly extract the maximum element and place it at the end.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_hs.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def heapify(arr, n, i):
    """Sift down element at index i in a max-heap of size n."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max-heap (heapify from last internal node up to root)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # move max to end
        heapify(arr, i, 0)                # restore heap property
    return arr

def solve(data):
    lines = data.splitlines()
    arr = list(map(int, lines[1].split()))
    print(' '.join(map(str, heap_sort(arr))))

if __name__ == '__main__':
    solve(get_input())
