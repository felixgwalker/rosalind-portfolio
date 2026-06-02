# Finding the Longest Multiple Repeat (MREP)
# Rosalind problem: https://rosalind.info/problems/mrep/
#
# Problem: Given a DNA string s and integer k, find the longest substring of s
# that appears at least k times (overlapping occurrences allowed).
#
# Algorithm:
#   1. Build suffix array (SA) via simple O(n log² n) prefix doubling.
#   2. Build LCP array via the Kasai algorithm.
#   3. Slide a window of k consecutive suffixes over SA; the minimum LCP in
#      the window of size (k-1) gives the length of their longest common prefix.
#      The maximum such minimum is the answer length.

import os
import sys
from collections import deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_mrep.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('>'):
            continue
        parts.append(line)
    return ''.join(parts)

def build_suffix_array(s):
    n = len(s)
    sa = sorted(range(n), key=lambda i: s[i:])
    return sa

def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i, v in enumerate(sa):
        rank[v] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    # First line = k, rest = FASTA or plain DNA string
    k = int(lines[0])
    rest = '\n'.join(lines[1:])
    s = parse_fasta(rest) if rest.startswith('>') else rest.replace('\n', '')

    if k <= 1:
        print(s)
        return

    n = len(s)
    sa  = build_suffix_array(s)
    lcp = build_lcp(s, sa)

    # Sliding window minimum over windows of size (k-1) in lcp[1..n-1]
    win = k - 1
    best_len = 0
    best_pos = 0
    dq = deque()  # monotone deque of indices into lcp (values ascending toward front)

    for i in range(1, n):
        # Maintain deque: remove larger values from back
        while dq and lcp[dq[-1]] >= lcp[i]:
            dq.pop()
        dq.append(i)
        # Window covers lcp[i-win+1 .. i] → SA indices i-win .. i
        if i >= win:
            while dq[0] < i - win + 1:
                dq.popleft()
            cur_min = lcp[dq[0]]
            if cur_min > best_len:
                best_len = cur_min
                best_pos = sa[i - win + 1]  # starting position of the repeated string

    if best_len == 0:
        print('')
    else:
        print(s[best_pos: best_pos + best_len])

if __name__ == '__main__':
    solve(get_input())
