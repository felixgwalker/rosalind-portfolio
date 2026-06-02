# BA1D — Find All Occurrences of a Pattern in a String
# https://rosalind.info/problems/ba1d/
#
# Given: a DNA string Pattern and a genome Text.
# Return: all starting positions (0-indexed) where Pattern appears in Text.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1d.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    pattern, text = lines[0].strip(), lines[1].strip()
    m = len(pattern)
    positions = [i for i in range(len(text) - m + 1) if text[i:i+m] == pattern]
    print(' '.join(map(str, positions)))

if __name__ == '__main__': solve(get_input())
