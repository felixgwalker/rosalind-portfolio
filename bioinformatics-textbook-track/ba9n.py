# BA9N — Find All Occurrences of a Collection of Patterns in a String Using BWT
# https://rosalind.info/problems/ba9n/
#
# Given: a string Text and patterns. Return: all starting positions using BWT+SA.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9n.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip() + '$'
    patterns = [l.strip() for l in lines[1:] if l.strip()]
    # Build suffix array and BWT
    n = len(text)
    sa = sorted(range(n), key=lambda i: text[i:])
    bwt = ''.join(text[sa[i]-1] if sa[i]>0 else text[-1] for i in range(n))
    first = sorted(bwt)
    first_occ = {}
    for i, ch in enumerate(first):
        if ch not in first_occ: first_occ[ch] = i
    counts = defaultdict(lambda: [0]*(n+1))
    for i, ch in enumerate(bwt):
        for c in counts: counts[c][i+1] = counts[c][i]
        counts[ch][i+1] = counts[ch][i] + 1
    positions = set()
    for pattern in patterns:
        top, bottom = 0, n-1
        for i in range(len(pattern)-1, -1, -1):
            symbol = pattern[i]
            if symbol not in first_occ: bottom = -1; break
            top = first_occ[symbol] + counts[symbol][top]
            bottom = first_occ[symbol] + counts[symbol][bottom+1] - 1
            if top > bottom: bottom = -1; break
        if top <= bottom:
            for i in range(top, bottom+1):
                positions.add(sa[i])
    print(' '.join(map(str, sorted(positions))))

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
