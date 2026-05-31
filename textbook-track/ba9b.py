# BA9B — Implement TrieMatching
# https://rosalind.info/problems/ba9b/
#
# Given: a string Text and a trie (as a list of patterns).
# Return: all starting positions in Text where a pattern from the collection matches.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9b.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip()
    patterns = [l.strip() for l in lines[1:] if l.strip()]
    pattern_set = set(patterns)
    results = []
    for i in range(len(text)):
        for p in patterns:
            if text[i:i+len(p)] == p:
                results.append(i)
                break
    print(' '.join(map(str, sorted(set(results)))))

if __name__ == '__main__': solve(get_input())
