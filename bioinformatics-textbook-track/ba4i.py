# BA4I — Implement ConvolutionCyclopeptideSequencing
# https://rosalind.info/problems/ba4i/
#
# Given: integers M and N, and a spectrum.
# Use the spectral convolution to determine the top-M most frequent amino acid masses,
# then run Leaderboard sequencing with leaderboard size N.

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4i.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def convolution_aa_masses(spectrum, M):
    """Return top-M amino acid masses from spectral convolution (range 57-200)."""
    diffs = Counter()
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            d = spectrum[j] - spectrum[i]
            if 57 <= d <= 200:
                diffs[d] += 1
    sorted_diffs = sorted(diffs.items(), key=lambda x: -x[1])
    if len(sorted_diffs) <= M:
        return list(diffs.keys())
    cutoff = sorted_diffs[M-1][1]
    return [d for d, c in sorted_diffs if c >= cutoff]

def cyclic_spectrum(masses):
    n = len(masses)
    if n == 0: return [0]
    prefix = [0] * (n+1)
    for i in range(n): prefix[i+1] = prefix[i] + masses[i]
    total = prefix[n]
    spec = [0, total]
    for length in range(1, n):
        for start in range(n):
            if start+length <= n:
                spec.append(prefix[start+length]-prefix[start])
            else:
                spec.append(total-prefix[start]+prefix[start+length-n])
    return sorted(spec)

def linear_spectrum(masses):
    n = len(masses)
    if n == 0: return [0]
    prefix = [0] * (n+1)
    for i in range(n): prefix[i+1] = prefix[i] + masses[i]
    spec = [0]
    for length in range(1, n+1):
        for start in range(n-length+1):
            spec.append(prefix[start+length]-prefix[start])
    return sorted(spec)

def score_cyclic(pep, spectrum):
    return sum(min(Counter(cyclic_spectrum(pep))[m], Counter(spectrum)[m]) for m in Counter(cyclic_spectrum(pep)))

def score_linear(pep, spectrum):
    return sum(min(Counter(linear_spectrum(pep))[m], Counter(spectrum)[m]) for m in Counter(linear_spectrum(pep)))

def trim(lb, spectrum, N):
    scores = sorted(lb, key=lambda p: -score_linear(p, spectrum))
    if len(scores) <= N: return scores
    cutoff = score_linear(scores[N-1], spectrum)
    return [p for p in scores if score_linear(p, spectrum) >= cutoff]

def solve(data):
    lines = data.splitlines()
    M, N = int(lines[0].strip()), int(lines[1].strip())
    spectrum = list(map(int, lines[2].split()))
    parent_mass = max(spectrum)
    aa_masses = list(set(convolution_aa_masses(spectrum, M)))

    leaderboard = [[]]
    leader_peptide, leader_score = [], 0

    while leaderboard:
        new_board = [pep + [m] for pep in leaderboard for m in aa_masses]
        leaderboard = []
        for pep in new_board:
            s = sum(pep)
            if s == parent_mass:
                sc = score_cyclic(pep, spectrum)
                if sc > leader_score:
                    leader_score, leader_peptide = sc, pep
            elif s < parent_mass:
                leaderboard.append(pep)
        leaderboard = trim(leaderboard, spectrum, N)

    print(' '.join(map(str, leader_peptide)))

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
