# Calculating Expected Offspring (IEV)
# Rosalind problem: https://rosalind.info/problems/iev/
#
# Problem: Given six non-negative integers representing the number of couples
# of each of the six possible genotype pairings (in order):
#   AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
# where each couple produces exactly 2 offspring, return the expected number
# of offspring displaying the dominant phenotype (at least one A allele).
#
# Algorithm: For each pairing, the probability that a child shows the dominant
# phenotype is known from Mendelian genetics. Multiply by 2 offspring and sum.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_iev.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

# P(dominant offspring) for each of the 6 mating types
# AA-AA: all children AA → 1.0
# AA-Aa: children are AA or Aa → 1.0
# AA-aa: all children Aa → 1.0
# Aa-Aa: 1/4 AA + 2/4 Aa + 1/4 aa → dominant = 3/4
# Aa-aa: 1/2 Aa + 1/2 aa → dominant = 1/2
# aa-aa: all children aa → 0.0
DOMINANT_PROBS = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

def solve(data):
    counts = list(map(int, data.split()))
    # Each couple has 2 offspring; expected dominant = count * 2 * P(dominant)
    expected = sum(c * 2 * p for c, p in zip(counts, DOMINANT_PROBS))
    print(expected)

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
