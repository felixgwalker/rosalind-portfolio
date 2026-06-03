# Locating Restriction Sites (REVP)
# Rosalind problem: https://rosalind.info/problems/revp/
#
# Problem: Given a DNA string in FASTA format, find all reverse palindromes of
# length 4 to 12. A reverse palindrome (restriction site) is a substring that
# equals its own reverse complement — the hallmark of Type II restriction enzyme
# recognition sequences (they cut at palindromic sites).
#
# Output: For each reverse palindrome, print its 1-based starting position and
# its length, sorted by position then length.
#
# Algorithm: Slide windows of each even length 4, 6, 8, 10, 12 across the
# sequence and check the palindrome condition. O(n · L) where L = 12.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_revp.txt')
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

COMP = str.maketrans('ACGT', 'TGCA')

def is_reverse_palindrome(s):
    """Return True if s equals its own reverse complement."""
    return s == s.translate(COMP)[::-1]

def solve(data):
    dna = parse_fasta(data)
    n = len(dna)
    results = []
    # Only even lengths 4..12 can be palindromes (odd-length palindromes don't
    # satisfy the reverse complement criterion for DNA)
    for length in range(4, 13, 2):
        for i in range(n - length + 1):
            if is_reverse_palindrome(dna[i:i+length]):
                results.append((i + 1, length))   # 1-indexed position

    results.sort()
    for pos, length in results:
        print(pos, length)

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
