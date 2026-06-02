# BA1M — Implement NumberToPattern
# https://rosalind.info/problems/ba1m/
#
# Given: an integer index and k.
# Return: the DNA string of length k that encodes this number (reverse of BA1L).
# The string is formed by treating index as a base-4 number with A=0, C=1, G=2, T=3.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1m.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

DIGITS = ['A', 'C', 'G', 'T']

def number_to_pattern(number, k):
    result = []
    for _ in range(k):
        result.append(DIGITS[number % 4])
        number //= 4
    return ''.join(reversed(result))

def solve(data):
    lines = data.splitlines()
    number, k = int(lines[0].strip()), int(lines[1].strip())
    print(number_to_pattern(number, k))

if __name__ == '__main__': solve(get_input())
