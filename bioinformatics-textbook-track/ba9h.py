# BA9H — Pattern Matching with the Suffix Array
# https://rosalind.info/problems/ba9h/
#
# Given: a string Text and a collection of patterns.
# Return: all positions where any pattern occurs in Text using suffix array binary search.

import os, sys
import bisect

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9h.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip()
    patterns = [l.strip() for l in lines[1:] if l.strip()]
    sa = sorted(range(len(text)), key=lambda i: text[i:])
    suffixes = [text[i:] for i in sa]
    positions = set()
    for p in patterns:
        lo = bisect.bisect_left(suffixes, p)
        hi = bisect.bisect_right(suffixes, p + '~')
        for i in range(lo, hi):
            if text[sa[i]:sa[i]+len(p)] == p:
                positions.add(sa[i])
    print(' '.join(map(str, sorted(positions))))

if __name__ == '__main__': solve(get_input())
