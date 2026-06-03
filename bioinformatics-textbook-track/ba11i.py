# BA11I — Compute the Size of a Spectral Dictionary
# https://rosalind.info/problems/ba11i/
#
# Given: A spectral vector Spectral, a score threshold T, and a max mass m.
# Return: The number of peptides of mass at most m scoring ≥ T against Spectral.
#
# We use DP: size[j] = number of distinct peptide paths reaching spectral
# position j with cumulative score ≥ T.  We count using prefix-score DP.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba11i.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

AA_MASSES = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def solve(data):
    lines = data.splitlines()
    spectral = list(map(int, lines[0].split()))
    T = int(lines[1].strip())
    max_mass = int(lines[2].strip())

    n = len(spectral)
    # dp[j] = list of prefix scores achievable when reaching position j
    # Use a counter: dp[j] maps score → count of paths with that score
    from collections import defaultdict
    dp = defaultdict(lambda: defaultdict(int))
    dp[0][0] = 1  # one way to reach position 0 with score 0

    total = 0

    for j in range(1, min(n, max_mass) + 1):
        gain = spectral[j - 1]
        for m in AA_MASSES:
            prev_j = j - m
            if prev_j < 0: continue
            for score, cnt in dp[prev_j].items():
                dp[j][score + gain] += cnt

    # Count paths reaching any position with score >= T
    for j in range(1, min(n, max_mass) + 1):
        for score, cnt in dp[j].items():
            if score >= T:
                total += cnt

    print(total)

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
