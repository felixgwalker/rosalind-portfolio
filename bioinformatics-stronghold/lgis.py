# Longest Increasing Subsequence (LGIS)
# Rosalind problem: https://rosalind.info/problems/lgis/
#
# Problem: Given a permutation of n integers (≤ 10000), output one longest
# strictly increasing subsequence and one longest strictly decreasing
# subsequence (any valid answer accepted).
#
# Algorithm: Patience sorting (O(n log n)) to find the LIS length and
# reconstruct one such subsequence. For LDS, negate each element and run LIS.
#
# Patience sorting maintains a list of "piles". Each new element goes on the
# leftmost pile whose top is ≥ the element (strict LIS). The number of piles
# equals the LIS length; the predecessor array enables reconstruction.

import os
import sys
import bisect

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_lgis.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def lis(seq):
    """Return one longest strictly increasing subsequence of seq."""
    if not seq:
        return []
    # tails[i] = smallest tail element of all LIS of length i+1 found so far
    tails = []
    # predecessor index for reconstruction
    pred = [-1] * len(seq)
    # index in seq of the element currently at tails[i]
    indices = []

    for i, x in enumerate(seq):
        # Find the leftmost tail that is >= x (bisect_left for strict increase)
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
            indices.append(i)
        else:
            tails[pos] = x
            indices[pos] = i
        # The predecessor of seq[i] is the element at position pos-1
        pred[i] = indices[pos - 1] if pos > 0 else -1

    # Reconstruct: start from the last element of the longest subsequence
    result = []
    k = indices[len(tails) - 1]   # index in seq of LIS tail
    while k != -1:
        result.append(seq[k])
        k = pred[k]
    return result[::-1]

def solve(data):
    lines = data.splitlines()
    seq = list(map(int, lines[1].split()))

    inc = lis(seq)
    # LDS = LIS of negated sequence, then negate back
    dec_raw = lis([-x for x in seq])
    dec = [-x for x in dec_raw]

    print(' '.join(map(str, inc)))
    print(' '.join(map(str, dec)))

if __name__ == '__main__':
    solve(get_input())
