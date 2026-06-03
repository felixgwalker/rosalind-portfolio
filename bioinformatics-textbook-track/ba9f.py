# BA9F — Find the Shortest Non-Shared Substring of Two Strings
# https://rosalind.info/problems/ba9f/
#
# Given: two strings s and t. Return: the shortest substring of s that does not appear in t.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9f.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    s, t = lines[0].strip(), lines[1].strip()
    # Binary search on length, then check
    for length in range(1, len(s)+1):
        for i in range(len(s)-length+1):
            sub = s[i:i+length]
            if sub not in t:
                print(sub); return

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
