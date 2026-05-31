# BA2H — Implement DistanceBetweenPatternAndStrings
# https://rosalind.info/problems/ba2h/
#
# Given: a k-mer Pattern and a list of DNA strings.
# Return: d(Pattern, Dna) = sum over all strings of the minimum Hamming distance
# from Pattern to any k-mer in that string.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba2h.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def solve(data):
    lines = data.splitlines()
    pattern = lines[0].strip()
    dna = [l.strip() for l in lines[1:] if l.strip()]
    k = len(pattern)
    total = sum(min(hamming(pattern, s[i:i+k]) for i in range(len(s)-k+1)) for s in dna)
    print(total)

if __name__ == '__main__': solve(get_input())
