# BA4D — Compute the Number of Peptides of Given Total Mass
# https://rosalind.info/problems/ba4d/
#
# Given: a positive integer m.
# Return: the number of linear peptides having integer mass equal to m,
# using the 20 amino acid masses from the standard monoisotopic table.
#
# Algorithm: DP counting. dp[mass] = number of ways to form a peptide of that mass.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

# Unique amino acid integer masses
AA_MASSES = list(set([57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]))

def solve(data):
    m = int(data.strip())
    dp = [0] * (m + 1)
    dp[0] = 1   # empty peptide has mass 0
    for mass in range(1, m + 1):
        for aa_mass in AA_MASSES:
            if mass >= aa_mass:
                dp[mass] += dp[mass - aa_mass]
    print(dp[m])

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
