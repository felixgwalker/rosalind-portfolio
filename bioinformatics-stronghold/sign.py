# Enumerating Oriented Gene Orderings (SIGN)
# Rosalind problem: https://rosalind.info/problems/sign/
#
# Problem: A signed permutation of length n is a permutation of {1,...,n} where
# each element has a sign (+ or -). Given n (≤ 6), output the total count
# (2^n × n!) followed by all signed permutations, one per line.
#
# Algorithm:
#   1. Generate all permutations of {1,...,n}.
#   2. For each permutation, generate all 2^n sign assignments.
#   Total: O(2^n × n! × n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_sign.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def permutations(items):
    if len(items) <= 1:
        yield list(items)
        return
    for i, item in enumerate(items):
        rest = items[:i] + items[i+1:]
        for perm in permutations(rest):
            yield [item] + perm

def solve(data):
    n = int(data.strip())
    items = list(range(1, n + 1))
    results = []

    for perm in permutations(items):
        # Generate all 2^n sign combinations using a bitmask
        for mask in range(1 << n):
            signed = []
            for bit, val in enumerate(perm):
                # If bit is set, element is negative
                signed.append(-val if (mask >> bit) & 1 else val)
            results.append(signed)

    print(len(results))
    for perm in results:
        print(' '.join(map(str, perm)))

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
