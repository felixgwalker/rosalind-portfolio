# Sex-Linked Inheritance (SEXL)
# Rosalind problem: https://rosalind.info/problems/sexl/
#
# Problem: For sex-linked traits (X-linked), given an array of frequencies of
# an X-linked recessive allele in females (same formula as Hardy-Weinberg),
# compute the probability that a randomly chosen female is a carrier (X^A X^a).
#
# Under Hardy-Weinberg for X-linked loci:
#   Males (XY): P(X^A Y) = p, P(X^a Y) = q, where p + q = 1
#   Females (XX): P(X^A X^A) = p², P(X^A X^a) = 2pq, P(X^a X^a) = q²
# Given the frequency of affected females P(X^a X^a) = q² = f, so q = sqrt(f).
# Carrier frequency = 2q(1-q) = 2*sqrt(f)*(1-sqrt(f)).

import os
import sys
import math

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_sexl.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    freqs = list(map(float, data.split()))
    results = []
    for f in freqs:
        q = math.sqrt(f)           # recessive allele frequency q
        carrier = 2 * q * (1 - q)  # heterozygous carrier frequency
        results.append(round(carrier, 3))
    print(' '.join(map(str, results)))

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
