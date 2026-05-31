# BA3L — Construct a String Spelled by a Gapped Genome Path
# https://rosalind.info/problems/ba3l/
#
# Given: integers k and d, and a sequence of (k,d)-mers forming a gapped path.
# Return: the string that this gapped path spells, if consistent; otherwise error.
#
# The string reconstructed from the prefix strand of the path must match the
# string reconstructed from the suffix strand (offset by k+d positions).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba3l.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    k, d = map(int, lines[0].split())
    pairs = [l.strip().split('|') for l in lines[1:] if l.strip()]

    prefix = pairs[0][0] + ''.join(a[-1] for a, b in pairs[1:])
    suffix = pairs[0][1] + ''.join(b[-1] for a, b in pairs[1:])

    # Verify consistency: prefix[k+d:] == suffix[:-(k+d)] = suffix[:len(suffix)-(k+d)]
    overlap = k + d
    if prefix[overlap:] == suffix[:-overlap] if overlap > 0 else prefix == suffix:
        print(prefix + suffix[-overlap:] if overlap > 0 else prefix)
    else:
        print("Inconsistent gapped path")

if __name__ == '__main__': solve(get_input())
