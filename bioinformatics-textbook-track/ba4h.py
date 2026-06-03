# BA4H — Generate the Convolution of a Spectrum
# https://rosalind.info/problems/ba4h/
#
# Given: a collection of integers representing a spectrum.
# Return: the list of elements in the Minkowski difference (spectral convolution),
# i.e., all positive pairwise differences, with multiplicity.

import os, sys
from collections import Counter

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba4h.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    spectrum = list(map(int, data.split()))
    diffs = Counter()
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            d = spectrum[j] - spectrum[i]
            if d > 0:
                diffs[d] += 1
    result = []
    for diff, count in sorted(diffs.items()):
        result.extend([diff] * count)
    print(' '.join(map(str, result)))

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
