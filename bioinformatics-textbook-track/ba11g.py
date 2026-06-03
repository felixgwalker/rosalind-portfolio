# BA11G — Implement PSMSearch
# https://rosalind.info/problems/ba11g/
#
# Given: A collection of spectral vectors, a proteome, and a score threshold.
# Return: A peptide-spectrum match (PSM) for each spectrum: the peptide from
#         the proteome scoring highest against that spectrum, if the score
#         meets or exceeds the threshold.
#
# Input format:
#   One spectral vector per line (space-separated integers), then "-------",
#   then protein lines, then "-------", then threshold.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba11g.txt')
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
        prefix += MASSES.get(aa, 0)
        if prefix > n: break
        score += spectral[prefix - 1]
    return score

def best_psm(spectral, proteome):
    n = len(spectral)
    best_sc = -float('inf')
    best_pep = ''
    for protein in proteome:
        for start in range(len(protein)):
            prefix = 0
            for end in range(start, len(protein)):
                prefix += MASSES.get(protein[end], 0)
                if prefix > n: break
                pep = protein[start:end + 1]
                sc = peptide_score(pep, spectral)
                if sc > best_sc:
                    best_sc = sc; best_pep = pep
    return best_pep, best_sc

def solve(data):
    sections = data.split('--------')
    spectra_lines = [l.strip() for l in sections[0].splitlines() if l.strip()]
    proteome = [l.strip() for l in sections[1].splitlines() if l.strip()]
    threshold = int(sections[2].strip())

    spectra = [list(map(int, l.split())) for l in spectra_lines]
    results = set()
    for spectral in spectra:
        pep, sc = best_psm(spectral, proteome)
        if sc >= threshold and pep:
            results.add(pep)

    for pep in sorted(results):
        print(pep)

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
