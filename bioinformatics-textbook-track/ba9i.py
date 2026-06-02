# BA9I — Construct the Burrows-Wheeler Transform of a String
# https://rosalind.info/problems/ba9i/
#
# Given: a DNA string s. Return: the BWT of s (last column of the cyclic rotation matrix).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9i.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def bwt(s):
    rotations = sorted(s[i:] + s[:i] for i in range(len(s)))
    return ''.join(r[-1] for r in rotations)

def solve(data):
    print(bwt(data.strip()))

if __name__ == '__main__': solve(get_input())
