# BA1C — Find the Reverse Complement of a DNA String
# https://rosalind.info/problems/ba1c/
#
# Given: a DNA string Pattern.
# Return: the reverse complement of Pattern.

import os, sys

COMP = str.maketrans('ACGTacgt', 'TGCAtgca')

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1c.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    print(data.strip().translate(COMP)[::-1])

if __name__ == '__main__': solve(get_input())
