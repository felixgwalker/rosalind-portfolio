# BA1G — Compute the Hamming Distance Between Two Strings
# https://rosalind.info/problems/ba1g/
#
# Given: two equal-length strings.
# Return: Hamming distance (number of positions where they differ).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1g.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    s, t = lines[0].strip(), lines[1].strip()
    print(sum(a != b for a, b in zip(s, t)))

if __name__ == '__main__': solve(get_input())
