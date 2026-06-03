# BA4G — Implement LeaderboardCyclopeptideSequencing
# https://rosalind.info/problems/ba4g/
#
# Given: integer N (leaderboard size) and a spectrum.
# Return: a cyclic peptide (space-separated masses) whose score against the spectrum
# is maximised using leaderboard pruning (top-N candidates kept each round).

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4g.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

AA_MASSES = list(set([57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]))

def cyclic_spectrum(masses):
    n = len(masses)
    if n == 0:
        return [0]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + masses[i]
    total = prefix[n]
    spec = [0, total]
    for length in range(1, n):
        for start in range(n):
            if start + length <= n:
                spec.append(prefix[start+length] - prefix[start])
            else:
                spec.append(total - prefix[start] + prefix[start+length-n])
    return sorted(spec)

def linear_spectrum(masses):
    n = len(masses)
    if n == 0:
        return [0]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + masses[i]
    spec = [0]
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            spec.append(prefix[start+length] - prefix[start])
    return sorted(spec)

def score_cyclic(peptide, spectrum):
    theo = Counter(cyclic_spectrum(peptide))
    real = Counter(spectrum)
    return sum(min(theo[m], real[m]) for m in theo)

def score_linear(peptide, spectrum):
    theo = Counter(linear_spectrum(peptide))
    real = Counter(spectrum)
    return sum(min(theo[m], real[m]) for m in theo)

def trim(leaderboard, spectrum, N):
    """Keep top-N peptides (plus ties at N-th place) by linear score."""
    scores = [(score_linear(pep, spectrum), pep) for pep in leaderboard]
    scores.sort(key=lambda x: -x[0])
    if len(scores) <= N:
        return [p for _, p in scores]
    cutoff = scores[N-1][0]
    return [p for s, p in scores if s >= cutoff]

def solve(data):
    lines = data.splitlines()
    N = int(lines[0].strip())
    spectrum = list(map(int, lines[1].split()))
    parent_mass = max(spectrum)

    leaderboard = [[]]
    leader_peptide = []
    leader_score = 0

    while leaderboard:
        # Expand
        new_board = []
        for pep in leaderboard:
            for mass in AA_MASSES:
                new_board.append(pep + [mass])
        leaderboard = new_board

        # Check and prune
        to_keep = []
        for pep in leaderboard:
            s = sum(pep)
            if s == parent_mass:
                sc = score_cyclic(pep, spectrum)
                if sc > leader_score:
                    leader_score = sc
                    leader_peptide = pep
            elif s < parent_mass:
                to_keep.append(pep)

        leaderboard = trim(to_keep, spectrum, N)

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
