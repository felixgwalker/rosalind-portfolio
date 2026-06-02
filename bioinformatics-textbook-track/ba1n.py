# BA1N — Generate the d-Neighborhood of a String
# https://rosalind.info/problems/ba1n/
#
# Given: a string Pattern and integer d.
# Return: the set of all strings within Hamming distance d of Pattern.
#
# Algorithm: Recursive enumeration — for each position, either keep the
# original base (not using any mismatch budget) or substitute a different
# base (using 1 mismatch). O(3^d * k * 4^(k-d)) time.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba1n.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def neighborhood(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return set('ACGT') if d >= 1 else {pattern}
    suffix_neighborhood = neighborhood(pattern[1:], d)
    result = set()
    for text in suffix_neighborhood:
        if hamming(pattern[1:], text) < d:
            for base in 'ACGT':
                result.add(base + text)
        else:
            result.add(pattern[0] + text)
    return result

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def solve(data):
    lines = data.splitlines()
    pattern, d = lines[0].strip(), int(lines[1].strip())
    result = sorted(neighborhood(pattern, d))
    print('\n'.join(result))

if __name__ == '__main__': solve(get_input())
