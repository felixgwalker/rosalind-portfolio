# BA2G — Implement GibbsSampler
# https://rosalind.info/problems/ba2g/
#
# Given: integers k, t, and N, and t DNA strings.
# Return: best motifs found by GibbsSampler run for N iterations.
#
# GibbsSampler randomly replaces one motif at a time using profile-based
# weighted random selection, allowing escape from local optima.

import os, sys, random

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba2g.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def build_profile_pseudo(motifs):
    k = len(motifs[0])
    t = len(motifs)
    return {b: [(sum(1 for m in motifs if m[j] == b) + 1)/(t+4) for j in range(k)] for b in 'ACGT'}

def score(motifs):
    k = len(motifs[0])
    return sum(len(motifs) - max(sum(1 for m in motifs if m[j]==b) for b in 'ACGT') for j in range(k))

def profile_random_kmer(text, k, profile):
    """Choose a k-mer from text weighted by its profile probability."""
    probs = []
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        p = 1.0
        for j, c in enumerate(kmer):
            p *= profile[c][j]
        probs.append(p)
    total = sum(probs)
    if total == 0:
        return text[random.randint(0, len(text)-k):][: k]
    r = random.uniform(0, total)
    cumsum = 0
    for i, p in enumerate(probs):
        cumsum += p
        if cumsum >= r:
            return text[i:i+k]
    return text[len(probs)-1:len(probs)-1+k]

def gibbs_sampler(dna, k, t, N):
    motifs = [s[random.randint(0, len(s)-k):random.randint(0, len(s)-k)+k] for s in dna]
    motifs = [s[i:i+k] for s, i in zip(dna, [random.randint(0, len(s)-k) for s in dna])]
    best = motifs[:]
    for _ in range(N):
        i = random.randint(0, t - 1)
        profile = build_profile_pseudo([motifs[j] for j in range(t) if j != i])
        motifs[i] = profile_random_kmer(dna[i], k, profile)
        if score(motifs) < score(best):
            best = motifs[:]
    return best

def solve(data):
    lines = data.splitlines()
    k, t, N = map(int, lines[0].split())
    dna = [l.strip() for l in lines[1:t+1] if l.strip()]
    random.seed(42)
    best = None
    for _ in range(20):
        motifs = gibbs_sampler(dna, k, t, N)
        if best is None or score(motifs) < score(best):
            best = motifs
    print('\n'.join(best))

if __name__ == '__main__':
    import io, contextlib
    data, out_path = get_input()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        solve(data)
    output = buf.getvalue()
    sys.stdout.write(output)
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(output)
