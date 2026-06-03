# BA9K — Generate the Last-to-First Mapping of a String
# https://rosalind.info/problems/ba9k/
#
# Given: BWT string and index i.
# Return: the position in the BWT that the last-to-first mapping sends row i to.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9k.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    bwt = lines[0].strip()
    i = int(lines[1].strip())
    first = sorted(bwt)
    # Count occurrences of bwt[i] in bwt[0..i]
    ch = bwt[i]
    rank = sum(1 for j in range(i+1) if bwt[j]==ch)
    # Find rank-th occurrence of ch in first column
    count = 0
    for j, c in enumerate(first):
        if c == ch:
            count += 1
            if count == rank:
                print(j); return

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
