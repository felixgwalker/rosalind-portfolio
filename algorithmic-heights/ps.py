# Partial Sort (PS)
# Rosalind problem: https://rosalind.info/problems/ps/
#
# Problem: Given an array of n integers and k, return the k smallest elements
# in sorted order.
# Algorithm: Min-heap selection (heapq.nsmallest). O(n log k).

import os
import sys
import heapq

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_ps.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    result = heapq.nsmallest(k, arr)
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
