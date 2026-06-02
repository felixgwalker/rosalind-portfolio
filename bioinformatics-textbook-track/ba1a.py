# BA1A — Count Occurrences of a Pattern in a String
# https://rosalind.info/problems/ba1a/
#
# Given: a DNA string Text and a pattern Pattern.
# Return: the number of times Pattern appears in Text (overlapping allowed).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1a.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    text, pattern = lines[0].strip(), lines[1].strip()
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    print(count)

if __name__ == '__main__': solve(get_input())
