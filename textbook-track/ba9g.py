# BA9G — Construct the Suffix Array of a String
# https://rosalind.info/problems/ba9g/
#
# Given: a DNA string s. Return: the suffix array (sorted order of all suffixes).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9g.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    s = data.strip()
    # Build suffix array: sort indices by their suffix
    sa = sorted(range(len(s)), key=lambda i: s[i:])
    print(', '.join(map(str, sa)))

if __name__ == '__main__': solve(get_input())
