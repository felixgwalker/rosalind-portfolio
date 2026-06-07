# Speeding Up Motif Finding — KMP Failure Array (KMP)
# Rosalind problem: https://rosalind.info/problems/kmp/
#
# Problem: Given a DNA string s in FASTA format, compute its failure array
# (prefix function). failure[i] is the length of the longest proper prefix of
# s[0..i] that is also a suffix of s[0..i].
#
# This array is the core of the Knuth-Morris-Pratt algorithm, enabling O(n+m)
# exact pattern matching (vs O(n·m) naive). The failure values tell the matcher
# how far back to slide the pattern on a mismatch without re-scanning.
#
# Algorithm: Standard KMP prefix-function construction — O(n) amortised.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_kmp.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read(), None

def parse_fasta(text):
    seq = []
    for line in text.splitlines():
        if not line.startswith('>'):
            seq.append(line.strip())
    return ''.join(seq)

def failure_array(s):
    """Compute the KMP prefix function for string s."""
    n = len(s)
    P = [0] * n    # P[0] = 0 always (no proper prefix for a single character)
    k = 0          # length of current longest matching proper prefix-suffix
    for i in range(1, n):
        # Fall back through the failure chain until we find a matching character
        # or exhaust all options (k becomes 0)
        while k > 0 and s[k] != s[i]:
            k = P[k - 1]
        if s[k] == s[i]:
            k += 1
        P[i] = k
    return P

def solve(data):
    s = parse_fasta(data)
    print(' '.join(map(str, failure_array(s))))

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
