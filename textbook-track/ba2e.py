# BA2E — Implement GreedyMotifSearch with Pseudocounts (Laplace's Rule)
# https://rosalind.info/problems/ba2e/
#
# Same as BA2D but with pseudocount of 1 added to every cell of the profile
# matrix (Laplace's Rule of Succession) to avoid zero probabilities.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba2e.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def build_profile_pseudo(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile = {}
    for base in 'ACGT':
        profile[base] = []
        for j in range(k):
            count = sum(1 for m in motifs if m[j] == base) + 1   # +1 pseudocount
            profile[base].append(count / (t + 4))   # divide by t + 4 (one extra per base)
    return profile

def profile_most_probable(text, k, profile):
    best_kmer, best_prob = text[:k], -1
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        p = 1.0
        for j, c in enumerate(kmer):
            p *= profile[c][j]
        if p > best_prob:
            best_prob = p
            best_kmer = kmer
    return best_kmer

def score(motifs):
    k = len(motifs[0])
    total = 0
    for j in range(k):
        counts = {b: sum(1 for m in motifs if m[j] == b) for b in 'ACGT'}
        total += len(motifs) - max(counts.values())
    return total

def greedy_motif_search_pseudo(dna, k, t):
    best_motifs = [s[:k] for s in dna]
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            profile = build_profile_pseudo(motifs)
            motifs.append(profile_most_probable(dna[j], k, profile))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

def solve(data):
    lines = data.splitlines()
    k, t = map(int, lines[0].split())
    dna = [l.strip() for l in lines[1:t+1] if l.strip()]
    motifs = greedy_motif_search_pseudo(dna, k, t)
    print('\n'.join(motifs))

if __name__ == '__main__': solve(get_input())
