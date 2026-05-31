# Enumerating k-mers Lexicographically (LEXF)
# Rosalind problem: https://rosalind.info/problems/lexf/
#
# Problem: Given an alphabet string (symbols space-separated on the first line)
# and a positive integer k on the second line, enumerate all strings of
# length k formed from the given symbols in lexicographic order.
#
# Algorithm: Recursive generation (depth-first enumeration). O(|alphabet|^k · k).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_lexf.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def enumerate_kmers(alphabet, k):
    """Yield all strings of length k over alphabet in lex order."""
    if k == 0:
        yield ''
        return
    for char in alphabet:
        for rest in enumerate_kmers(alphabet, k - 1):
            yield char + rest

def solve(data):
    lines = data.splitlines()
    alphabet = lines[0].split()   # space-separated symbols
    k = int(lines[1].strip())
    for kmer in enumerate_kmers(alphabet, k):
        print(kmer)

if __name__ == '__main__':
    solve(get_input())
