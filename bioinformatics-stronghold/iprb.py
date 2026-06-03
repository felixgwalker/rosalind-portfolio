# Mendel's First Law (IPRB)
# Rosalind problem: https://rosalind.info/problems/iprb/
#
# Problem: A population contains k homozygous dominant (YY), m heterozygous
# (Yy), and n homozygous recessive (yy) organisms. Two are chosen at random
# to mate. Return the probability their offspring carries at least one dominant
# allele (dominant or heterozygous phenotype/genotype).
#
# Algorithm: P(dominant) = 1 − P(recessive offspring, i.e. yy).
# A yy child requires both parents to contribute a y allele:
#   yy × yy  → P(yy child) = 1.0
#   yy × Yy  → P(yy child) = 0.5  (both selection orders included)
#   Yy × Yy  → P(yy child) = 0.25
# Sampling is without replacement, so parent selection uses falling factorials.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_iprb.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    k, m, n = map(int, data.split())   # YY, Yy, yy counts
    total = k + m + n

    # Probability of picking each ordered pair of parents
    def pick2(a, b):
        """P(first parent from group a, second from group b), without replacement."""
        if a == b:
            return (a / total) * ((a - 1) / (total - 1))
        return (a / total) * (b / (total - 1))

    p_recessive = (
        pick2(n, n) * 1.0    +   # yy × yy: all offspring yy
        pick2(n, m) * 0.5    +   # yy × Yy: half offspring yy
        pick2(m, n) * 0.5    +   # Yy × yy: half offspring yy
        pick2(m, m) * 0.25       # Yy × Yy: quarter offspring yy
    )

    print(1 - p_recessive)

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
