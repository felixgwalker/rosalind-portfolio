# BA2F — Implement RandomizedMotifSearch
# https://rosalind.info/problems/ba2f/
#
# Given: integers k and t, and t DNA strings.
# Return: a collection of k-mers (motifs) found by RandomizedMotifSearch.
#
# RandomizedMotifSearch:
#   1. Randomly choose one k-mer from each string as initial motifs.
#   2. Repeat until no improvement:
#      a. Build profile from current motifs.
#      b. For each string, pick the most probable k-mer (using pseudocounts).
#   The best motif set across many random restarts is returned.
#
# Note: Results are non-deterministic; we run 1000 iterations for quality.

import os, sys, random

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba2f.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def build_profile_pseudo(motifs):
    k = len(motifs[0])
    t = len(motifs)
    return {base: [(sum(1 for m in motifs if m[j] == base) + 1) / (t + 4) for j in range(k)] for base in 'ACGT'}

def profile_most_probable(text, k, profile):
    best_kmer, best_prob = text[:k], -1.0
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        p = 1.0
        for j, c in enumerate(kmer):
            p *= profile[c][j]
        if p > best_prob:
            best_prob, best_kmer = p, kmer
    return best_kmer

def score(motifs):
    k = len(motifs[0])
    return sum(len(motifs) - max(sum(1 for m in motifs if m[j] == b) for b in 'ACGT') for j in range(k))

def randomized_motif_search(dna, k, t):
    motifs = [s[random.randint(0, len(s)-k):random.randint(0, len(s)-k)+k] for s in dna]
    # Ensure valid k-mers
    motifs = [s[random.randint(0, len(s)-k)] + s[random.randint(0, len(s)-k)+1:random.randint(0, len(s)-k)+k] for s in dna]
    motifs = [s[i:i+k] for s, i in zip(dna, [random.randint(0, len(s)-k) for s in dna])]
    best = motifs[:]
    while True:
        profile = build_profile_pseudo(motifs)
        motifs = [profile_most_probable(s, k, profile) for s in dna]
        if score(motifs) < score(best):
            best = motifs[:]
        else:
            return best

def solve(data):
    lines = data.splitlines()
    k, t = map(int, lines[0].split())
    dna = [l.strip() for l in lines[1:t+1] if l.strip()]
    random.seed(42)
    best = None
    for _ in range(1000):
        motifs = randomized_motif_search(dna, k, t)
        if best is None or score(motifs) < score(best):
            best = motifs
    print('\n'.join(best))

if __name__ == '__main__': solve(get_input())
