# BA2C — Find a Profile-Most Probable k-mer in a String
# https://rosalind.info/problems/ba2c/
#
# Given: a string Text, integer k, and a 4×k profile matrix (rows A, C, G, T).
# Return: the k-mer in Text that is most probable under the profile.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba2c.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def profile_prob(kmer, profile):
    """Probability of k-mer given profile dict {base: [probs]}."""
    p = 1.0
    for i, c in enumerate(kmer):
        p *= profile[c][i]
    return p

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip()
    k = int(lines[1].strip())
    rows = [list(map(float, lines[2+i].split())) for i in range(4)]
    profile = {'A': rows[0], 'C': rows[1], 'G': rows[2], 'T': rows[3]}

    best_kmer, best_prob = '', -1
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        p = profile_prob(kmer, profile)
        if p > best_prob:
            best_prob = p
            best_kmer = kmer
    print(best_kmer)

if __name__ == '__main__': solve(get_input())
