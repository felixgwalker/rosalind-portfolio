# BA11F — Find a Highest-Scoring Peptide in a Proteome against a Spectrum
# https://rosalind.info/problems/ba11f/
#
# Given: A spectral vector Spectral and a proteome (one protein per line).
# Return: A peptide from the proteome with maximum score against Spectral.
#
# We slide a window of every possible length over each protein string and
# score each substring's peptide vector against the spectral vector.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba11f.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MASSES = {
    'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
    'N':114,'D':115,'Q':128,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
}

def peptide_score(peptide, spectral):
    n = len(spectral)
    prefix = 0
    score = 0
    for aa in peptide:
        prefix += MASSES[aa]
        if prefix > n: break
        score += spectral[prefix - 1]  # 1-indexed prefix mass → 0-indexed spectral
    return score

def solve(data):
    lines = data.splitlines()
    spectral = list(map(int, lines[0].split()))
    proteome = [l.strip() for l in lines[1:] if l.strip()]
    n = len(spectral)

    best_score = -float('inf')
    best_peptide = ''

    for protein in proteome:
        for start in range(len(protein)):
            prefix = 0
            for end in range(start, len(protein)):
                prefix += MASSES.get(protein[end], 0)
                if prefix > n: break
                peptide = protein[start:end + 1]
                sc = peptide_score(peptide, spectral)
                if sc > best_score:
                    best_score = sc
                    best_peptide = peptide

    print(best_peptide)

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
