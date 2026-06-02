# BA1K — Generate the Frequency Array of a String
# https://rosalind.info/problems/ba1k/
#
# Given: a DNA string Text and integer k.
# Return: the frequency array of Text: an array of length 4^k where entry i
# equals the number of occurrences of NumberToPattern(i, k) in Text.
# Index i corresponds to the k-mer encoded as base-4 number (A=0, C=1, G=2, T=3).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1k.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

BASE = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def pattern_to_number(pattern):
    n = 0
    for c in pattern:
        n = n * 4 + BASE[c]
    return n

def solve(data):
    lines = data.splitlines()
    text, k = lines[0].strip(), int(lines[1].strip())
    freq = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        freq[pattern_to_number(text[i:i+k])] += 1
    print(' '.join(map(str, freq)))

if __name__ == '__main__': solve(get_input())
