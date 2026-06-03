# BA4J — Generate the Theoretical Spectrum of a Linear Peptide
# https://rosalind.info/problems/ba4j/
#
# Given: An amino acid string Peptide.
# Return: The linear spectrum of Peptide.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4j.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MASSES = {
    'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
    'N':114,'D':115,'Q':128,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
}

def linear_spectrum(peptide):
    masses = [MASSES[aa] for aa in peptide]
    n = len(masses)
    prefix = [0] * (n + 1)
    for i in range(n): prefix[i+1] = prefix[i] + masses[i]
    spec = [0]
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            spec.append(prefix[start + length] - prefix[start])
    return sorted(spec)

def solve(data):
    print(' '.join(map(str, linear_spectrum(data.strip()))))

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
