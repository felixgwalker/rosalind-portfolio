# BA4C — Generate the Theoretical Spectrum of a Cyclic Peptide
# https://rosalind.info/problems/ba4c/
#
# Given: an amino acid string Peptide (using integer masses or letter codes).
# Return: the theoretical spectrum (sorted list of all subpeptide masses, including 0
# and the full peptide mass).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4c.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

MONO_MASS = {
    'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,
    'D':115,'Q':128,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
}

def cyclic_spectrum(peptide):
    n = len(peptide)
    masses = [MONO_MASS[aa] for aa in peptide]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + masses[i]
    total = prefix[n]
    spectrum = [0]
    for length in range(1, n):
        for start in range(n):
            sub_mass = prefix[start+length] - prefix[start] if start+length <= n else total - (prefix[n] - prefix[start+length-n])
            if start + length > n:
                sub_mass = total - (prefix[n] - prefix[start + length - n]) + prefix[start] - prefix[start]
                sub_mass = prefix[start + length - n] + total - prefix[start]
            spectrum.append(sub_mass)
    spectrum.append(total)
    return sorted(spectrum)

def solve(data):
    peptide = data.strip()
    # Handle integer input (masses separated by spaces)
    if ' ' in peptide or any(c.isdigit() for c in peptide):
        masses = list(map(int, peptide.split()))
        n = len(masses)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + masses[i]
        total = prefix[n]
        spectrum = [0, total]
        for length in range(1, n):
            for start in range(n):
                if start + length <= n:
                    spectrum.append(prefix[start+length] - prefix[start])
                else:
                    spectrum.append(total - prefix[start] + prefix[start+length-n])
        print(' '.join(map(str, sorted(spectrum))))
    else:
        print(' '.join(map(str, cyclic_spectrum(peptide))))

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
