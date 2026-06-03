# BA1E — Find Patterns Forming Clumps in a String
# https://rosalind.info/problems/ba1e/
#
# Given: a string Genome and integers k, L, t.
# Return: all distinct k-mers that appear at least t times in some window of length L.
#
# Algorithm: Sliding window of length L with a frequency dict. O(n·k) time.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba1e.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def find_clumps(genome, k, L, t):
    clumps = set()
    freq = defaultdict(int)
    n = len(genome)

    # Initialise the first window
    for i in range(L - k + 1):
        freq[genome[i:i+k]] += 1

    for kmer, cnt in freq.items():
        if cnt >= t:
            clumps.add(kmer)

    # Slide the window
    for i in range(1, n - L + 1):
        # Remove outgoing k-mer
        outgoing = genome[i-1:i-1+k]
        freq[outgoing] -= 1
        # Add incoming k-mer
        incoming = genome[i+L-k:i+L]
        freq[incoming] += 1
        if freq[incoming] >= t:
            clumps.add(incoming)

    return clumps

def solve(data):
    lines = data.splitlines()
    genome = lines[0].strip()
    k, L, t = map(int, lines[1].split())
    result = sorted(find_clumps(genome, k, L, t))
    print(' '.join(result))

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
