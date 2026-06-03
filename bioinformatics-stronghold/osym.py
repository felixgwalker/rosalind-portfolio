# Counting Palindromic Substrings (OSYM)
# Rosalind problem: https://rosalind.info/problems/osym/
#
# Problem: Given a DNA string (in FASTA), count the total number of substrings
# that are Watson–Crick palindromes (i.e., the string equals its own reverse
# complement).  Only even-length substrings can be WC palindromes for the
# 4-character DNA alphabet.
#
# Algorithm: O(n²) scan: for each starting index i and each even length L ≥ 2,
# check whether s[i:i+L] == rev_comp(s[i:i+L]).  Equivalently, expand
# outward from each midpoint as long as s[l] == comp[s[r]].

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_osym.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('>'):
            continue
        parts.append(line)
    return ''.join(parts)

COMP = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def solve(data):
    s = parse_fasta(data) if '>' in data else data.strip()
    n = len(s)
    count = 0
    # Expand around each gap between adjacent characters (even-length palindromes)
    for mid in range(n - 1):
        l, r = mid, mid + 1
        while l >= 0 and r < n and s[l] == COMP.get(s[r], ''):
            count += 1
            l -= 1
            r += 1
    print(count)

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
