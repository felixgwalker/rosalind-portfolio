# Introduction to Random Strings (PROB)
# Rosalind problem: https://rosalind.info/problems/prob/
#
# Problem: Given a DNA string s and an array A of GC-content values, for each
# value x in A compute the log₁₀ probability that a random genome with that GC
# content would match s exactly, assuming each position is independently drawn.
#
# Model: Under GC content x,
#   P(G) = P(C) = x/2
#   P(A) = P(T) = (1-x)/2
# Work in log space to avoid numerical underflow for long strings.
#
# Output: space-separated log₁₀ probabilities (rounded to 3 decimal places).

import os
import sys
import math

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_prob.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    s = lines[0].strip()
    gc_values = list(map(float, lines[1].split()))

    results = []
    for x in gc_values:
        log_p = 0.0
        for base in s:
            if base in 'GC':
                log_p += math.log10(x / 2)
            else:             # A or T
                log_p += math.log10((1 - x) / 2)
        results.append(round(log_p, 3))

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
