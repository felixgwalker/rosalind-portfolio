# BA2A — Implement MotifEnumeration
# https://rosalind.info/problems/ba2a/
#
# Given: integers k and d, and a list of DNA strings.
# Return: all (k, d)-motifs — k-mers that appear in every string with ≤ d mismatches.
#
# Algorithm: For each string, enumerate all k-mers and their d-neighborhoods.
# The intersection of these neighborhoods across all strings gives the motifs.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba2a.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def neighbors(pattern, d):
    if d == 0:
        yield pattern; return
    for i in range(len(pattern)):
        for base in 'ACGT':
            if base != pattern[i]:
                for rest in neighbors(pattern[:i] + base + pattern[i+1:], d - 1):
                    yield rest
                    return
    yield pattern   # fallback

def neighborhood(pattern, d):
    """All strings within Hamming distance d of pattern."""
    if d == 0:
        return {pattern}
    if len(pattern) == 0:
        return {''}
    suffix_nb = neighborhood(pattern[1:], d)
    result = set()
    for text in suffix_nb:
        if hamming(pattern[1:], text) < d:
            for base in 'ACGT':
                result.add(base + text)
        else:
            result.add(pattern[0] + text)
    return result

def motif_enumeration(dna, k, d):
    patterns = set()
    for text in dna:
        for i in range(len(text) - k + 1):
            for pattern in neighborhood(text[i:i+k], d):
                if all(min(hamming(pattern, s[j:j+k]) for j in range(len(s)-k+1)) <= d for s in dna):
                    patterns.add(pattern)
    return patterns

def solve(data):
    lines = data.splitlines()
    k, d = map(int, lines[0].split())
    dna = [l.strip() for l in lines[1:] if l.strip()]
    result = sorted(motif_enumeration(dna, k, d))
    print(' '.join(result))

if __name__ == '__main__': solve(get_input())
