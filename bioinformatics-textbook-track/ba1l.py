# BA1L — Implement PatternToNumber
# https://rosalind.info/problems/ba1l/
#
# Given: a DNA string Pattern.
# Return: the integer encoding of Pattern using A=0, C=1, G=2, T=3 as base-4 digits.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1l.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

BASE = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def solve(data):
    pattern = data.strip()
    n = 0
    for c in pattern:
        n = n * 4 + BASE[c]
    print(n)

if __name__ == '__main__': solve(get_input())
