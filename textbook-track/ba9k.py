# BA9K — Generate the Last-to-First Mapping of a String
# https://rosalind.info/problems/ba9k/
#
# Given: BWT string and index i.
# Return: the position in the BWT that the last-to-first mapping sends row i to.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9k.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    bwt = lines[0].strip()
    i = int(lines[1].strip())
    first = sorted(bwt)
    # Count occurrences of bwt[i] in bwt[0..i]
    ch = bwt[i]
    rank = sum(1 for j in range(i+1) if bwt[j]==ch)
    # Find rank-th occurrence of ch in first column
    count = 0
    for j, c in enumerate(first):
        if c == ch:
            count += 1
            if count == rank:
                print(j); return

if __name__ == '__main__': solve(get_input())
