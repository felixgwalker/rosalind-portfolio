# Introduction to Set Operations (SETO)
# Rosalind problem: https://rosalind.info/problems/seto/
#
# Problem: Given n and two sets A and B (both subsets of {1,...,n}), output the
# results of six set operations:
#   1. A ∪ B   (union)
#   2. A ∩ B   (intersection)
#   3. A \ B   (set difference: elements in A but not B)
#   4. B \ A   (set difference: elements in B but not A)
#   5. Ā       (complement of A in {1,...,n})
#   6. B̄       (complement of B in {1,...,n})
# Each set is output as a space-separated list inside curly braces, sorted.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_seto.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_set(s):
    """Parse '{1, 2, 3}' into a Python set of ints."""
    s = s.strip().strip('{}')
    if not s.strip():
        return set()
    return set(map(int, s.split(',')))

def fmt_set(s):
    """Format a set of ints as '{1, 2, 3}' in sorted order."""
    return '{' + ', '.join(map(str, sorted(s))) + '}'

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    A = parse_set(lines[1])
    B = parse_set(lines[2])
    universe = set(range(1, n + 1))

    print(fmt_set(A | B))        # union
    print(fmt_set(A & B))        # intersection
    print(fmt_set(A - B))        # A minus B
    print(fmt_set(B - A))        # B minus A
    print(fmt_set(universe - A)) # complement of A
    print(fmt_set(universe - B)) # complement of B

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
