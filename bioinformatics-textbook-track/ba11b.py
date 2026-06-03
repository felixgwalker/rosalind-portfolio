# BA11B — Implement DeNovoSequencing
# https://rosalind.info/problems/ba11b/
#
# Given: A collection of integers Spectrum.
# Return: An amino acid string with maximum score against Spectrum among all
#         amino acid strings with total mass equal to the largest mass in Spectrum.
#
# We build the spectrum graph (a DAG), find the longest (max-score) path
# from 0 to parent_mass, then reconstruct the peptide.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba11b.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MASS_TO_AA = {
    57:'G', 71:'A', 87:'S', 97:'P', 99:'V', 101:'T', 103:'C',
    113:'L', 114:'N', 115:'D', 128:'Q', 129:'E', 131:'M',
    137:'H', 147:'F', 156:'R', 163:'Y', 186:'W'
}

def solve(data):
    spectrum = sorted(set(map(int, data.split())))
    spec_set = set(spectrum)
    parent = max(spectrum)
    nodes = sorted(spec_set | {0})

    # dp[m] = (score, prev_mass, aa_label) for the best path reaching mass m
    dp = {m: (-1, None, None) for m in nodes}
    dp[0] = (0, None, None)

    for j in nodes:
        if j == 0: continue
        for i in nodes:
            if i >= j: break
            diff = j - i
            if diff in MASS_TO_AA and dp[i][0] >= 0:
                score = dp[i][0] + (1 if j in spec_set else 0)
                if score > dp[j][0]:
                    dp[j] = (score, i, MASS_TO_AA[diff])

    # Reconstruct path
    if dp[parent][0] < 0:
        print("")
        return
    peptide = []
    cur = parent
    while dp[cur][1] is not None:
        peptide.append(dp[cur][2])
        cur = dp[cur][1]
    print(''.join(reversed(peptide)))

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
