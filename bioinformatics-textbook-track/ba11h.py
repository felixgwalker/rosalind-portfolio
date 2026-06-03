# BA11H — Implement Spectral Alignment
# https://rosalind.info/problems/ba11h/
#
# Given: A peptide Peptide, a spectral vector Spectral, and an integer k.
# Return: A highest-scoring modification of Peptide with at most k modifications,
#         i.e., the modified peptide (as a sequence of amino acid masses) that
#         best explains Spectral.
#
# We use 2-D dynamic programming: dp[i][j] = best score using the first i
# characters of Peptide and reaching spectral position j, allowing at most
# the modifications encountered so far. An "unmodified" step uses the real
# amino acid mass; a "modified" step can step any positive integer.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba11h.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MASSES = {
    'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
    'N':114,'D':115,'Q':128,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
}

def solve(data):
    lines = data.splitlines()
    peptide = lines[0].strip()
    spectral = list(map(int, lines[1].split()))
    k = int(lines[2].strip())

    n = len(peptide)
    m = len(spectral)
    pep_masses = [MASSES[aa] for aa in peptide]
    # dp[i][j] = best score when we've processed peptide[0..i-1] and reached spectral position j
    NEG = float('-inf')
    dp = [[NEG] * (m + 1) for _ in range(n + 1)]
    mods = [[0] * (m + 1) for _ in range(n + 1)]   # number of modifications used
    prev = [[None] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 0

    for i in range(n):
        mass_i = pep_masses[i]
        for j in range(m + 1):
            if dp[i][j] == NEG: continue
            # Option 1: place amino acid i unmodified at position j → j + mass_i
            nj = j + mass_i
            if nj <= m:
                gain = spectral[nj - 1] if nj > 0 else 0
                score = dp[i][j] + gain
                if score > dp[i+1][nj] or (score == dp[i+1][nj] and mods[i][j] < mods[i+1][nj]):
                    dp[i+1][nj] = score
                    mods[i+1][nj] = mods[i][j]
                    prev[i+1][nj] = (i, j, mass_i)
            # Option 2: modify amino acid i (any positive step size) — costs one modification
            if mods[i][j] < k:
                for nj2 in range(j + 1, m + 1):
                    gain = spectral[nj2 - 1] if nj2 > 0 else 0
                    score = dp[i][j] + gain
                    if score > dp[i+1][nj2]:
                        dp[i+1][nj2] = score
                        mods[i+1][nj2] = mods[i][j] + 1
                        prev[i+1][nj2] = (i, j, nj2 - j)

    # Find best ending position
    best_score = NEG
    best_j = -1
    for j in range(m + 1):
        if dp[n][j] > best_score:
            best_score = dp[n][j]
            best_j = j

    # Reconstruct path of masses
    result_masses = []
    ci, cj = n, best_j
    while prev[ci][cj] is not None:
        pi, pj, mass = prev[ci][cj]
        result_masses.append(mass)
        ci, cj = pi, pj
    result_masses.reverse()
    print(' '.join(map(str, result_masses)))

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
