# BA3A — Generate the k-mer Composition of a String
# https://rosalind.info/problems/ba3a/
#
# Given: an integer k and a DNA string Text.
# Return: the k-mer composition of Text: all k-mers in lexicographic order (with multiplicity).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3a.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    k, text = int(lines[0].strip()), lines[1].strip()
    kmers = sorted(text[i:i+k] for i in range(len(text) - k + 1))
    print('\n'.join(kmers))

if __name__ == '__main__': solve(get_input())
