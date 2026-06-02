# BA6E — Find All Shared k-mers of a Pair of Strings
# https://rosalind.info/problems/ba6e/
#
# Given: an integer k and two strings s and t.
# Return: all (i, j) pairs (0-indexed) where s[i:i+k] == t[j:j+k] or
# is the reverse complement of t[j:j+k].

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba6e.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

COMP = str.maketrans('ACGT','TGCA')

def solve(data):
    lines = data.splitlines()
    k, s, t = int(lines[0].strip()), lines[1].strip(), lines[2].strip()
    # Index t k-mers by value → list of positions
    t_index = {}
    for j in range(len(t)-k+1):
        km = t[j:j+k]
        t_index.setdefault(km, []).append(j)
        rc = km.translate(COMP)[::-1]
        t_index.setdefault(rc, []).append(j)
    pairs = []
    for i in range(len(s)-k+1):
        km = s[i:i+k]
        for j in t_index.get(km, []):
            pairs.append((i, j))
    for pair in sorted(set(pairs)):
        print(pair)

if __name__ == '__main__': solve(get_input())
