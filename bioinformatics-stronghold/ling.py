# Linguistic Complexity of a Genome (LING)
# Rosalind problem: https://rosalind.info/problems/ling/
#
# Problem: The linguistic complexity of a string s is the ratio of the number
# of distinct substrings of s to the maximum number of distinct substrings
# possible for a string of that length over a 4-letter alphabet (ACGT).
#
# Max distinct substrings for length n over alphabet size k = 4:
#   sum_{L=1}^{n} min(n - L + 1, k^L)
#
# Distinct substrings = number of unique substrings of all lengths 1 to n.
# For small strings (≤ 1000 nt), a set-based approach is feasible.
# For larger strings, a suffix array + LCP array would be needed.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_ling.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        if not line.startswith('>'):
            parts.append(line.strip())
    return ''.join(parts)

def solve(data):
    s = parse_fasta(data)
    n = len(s)
    k = 4   # alphabet size (ACGT)

    # Count distinct substrings
    distinct = set()
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            distinct.add(s[i:i+length])
    actual = len(distinct)

    # Maximum possible distinct substrings
    maximum = sum(min(n - L + 1, k ** L) for L in range(1, n + 1))

    print(round(actual / maximum, 6))

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
