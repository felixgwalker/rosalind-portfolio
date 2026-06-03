# BA5G — Compute the Edit Distance Between Two Strings
# https://rosalind.info/problems/ba5g/
#
# Given: two strings. Return: their Levenshtein edit distance.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba5g.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines(); s, t = lines[0].strip(), lines[1].strip()
    m, n = len(s), len(t)
    prev = list(range(n+1))
    for i in range(1, m+1):
        curr = [i] + [0]*n
        for j in range(1, n+1):
            curr[j] = prev[j-1] if s[i-1]==t[j-1] else 1+min(prev[j-1], prev[j], curr[j-1])
        prev = curr
    print(prev[n])

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
