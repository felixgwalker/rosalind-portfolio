# BA4E — Find a Cyclopeptide with Theoretical Spectrum Matching an Ideal Spectrum
# https://rosalind.info/problems/ba4e/
#
# Given: a collection of (possibly repeated) integers representing a spectrum.
# Return: a cyclic peptide (as space-separated integer masses) whose theoretical
# spectrum matches the given spectrum exactly.
#
# Algorithm: Branch-and-bound cyclopeptide sequencing.
#   - Grow candidate peptides one amino acid at a time.
#   - Prune candidates whose linear spectrum is not consistent with the given spectrum.
#   - Output any peptide whose cyclic spectrum matches exactly.

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4e.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

AA_MASSES = list(set([57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]))

def cyclic_spectrum(masses):
    n = len(masses)
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
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + masses[i]
    spec = [0]
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            spec.append(prefix[start+length] - prefix[start])
    return sorted(spec)

def is_consistent(peptide, spectrum_count):
    lin = Counter(linear_spectrum(peptide))
    return all(lin[m] <= spectrum_count[m] for m in lin)

def solve(data):
    spectrum = list(map(int, data.split()))
    spectrum_count = Counter(spectrum)
    parent_mass = max(spectrum)

    candidates = [[]]
    final = []

    while candidates:
        new_candidates = []
        for pep in candidates:
            for mass in AA_MASSES:
                new_pep = pep + [mass]
                if sum(new_pep) == parent_mass:
                    if cyclic_spectrum(new_pep) == spectrum:
                        final.append(new_pep)
                elif sum(new_pep) < parent_mass and is_consistent(new_pep, spectrum_count):
                    new_candidates.append(new_pep)
        candidates = new_candidates

    if final:
        print(' '.join(map(str, final[0])))

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
