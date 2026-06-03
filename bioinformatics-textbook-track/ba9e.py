# BA9E — Find the Longest Substring Shared by Two Strings
# https://rosalind.info/problems/ba9e/
#
# Given: two strings. Return: the longest common substring.
# Algorithm: suffix array on concatenation s#t$, find LCP between cross-string suffixes.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9e.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    s, t = lines[0].strip(), lines[1].strip()
    n, m = len(s), len(t)
    combined = s + '#' + t + '$'
    sa = sorted(range(len(combined)), key=lambda i: combined[i:])
    best_len = 0; best = ''
    for i in range(1, len(sa)):
        a_idx, b_idx = sa[i-1], sa[i]
        # Check cross-string
        a_in_s = a_idx < n; b_in_s = b_idx < n
        if a_in_s != b_in_s:
            a = combined[a_idx:]; b = combined[b_idx:]
            k = 0
            while k < min(len(a),len(b)) and a[k]==b[k] and a[k] not in '#$':
                k += 1
            if k > best_len: best_len = k; best = a[:k]
    print(best)

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
