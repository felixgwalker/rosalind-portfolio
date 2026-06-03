# BA1F — Find a Position in a Genome Minimizing the Skew
# https://rosalind.info/problems/ba1f/
#
# Problem: The skew of a genome prefix of length i is #G - #C in that prefix.
# Find all positions where the skew reaches its minimum.
#
# Output: 0-indexed positions (space-separated) where skew is minimised.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba1f.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    genome = data.strip()
    skew = [0] * (len(genome) + 1)
    for i, c in enumerate(genome):
        if c == 'G':
            skew[i+1] = skew[i] + 1
        elif c == 'C':
            skew[i+1] = skew[i] - 1
        else:
            skew[i+1] = skew[i]
    min_skew = min(skew)
    positions = [i for i, s in enumerate(skew) if s == min_skew]
    print(' '.join(map(str, positions)))

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
