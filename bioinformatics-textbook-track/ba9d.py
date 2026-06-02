# BA9D — Find the Longest Repeat in a String
# https://rosalind.info/problems/ba9d/
#
# Given: a DNA string. Return: the longest repeat (substring appearing ≥ twice).
# Algorithm: build suffix array + LCP array, find max LCP value.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9d.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    s = data.strip() + '$'
    n = len(s)
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build LCP array
    best_len = 0; best = ''
    for i in range(1, len(sa)):
        a, b = s[sa[i-1]:], s[sa[i]:]
        k = 0
        while k < min(len(a),len(b)) and a[k] == b[k]:
            k += 1
        if k > best_len:
            best_len = k; best = a[:k]
    print(best)

if __name__ == '__main__': solve(get_input())
