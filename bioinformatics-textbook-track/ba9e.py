# BA9E — Find the Longest Substring Shared by Two Strings
# https://rosalind.info/problems/ba9e/
#
# Given: two strings. Return: the longest common substring.
# Algorithm: suffix array on concatenation s#t$, find LCP between cross-string suffixes.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9e.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

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

if __name__ == '__main__': solve(get_input())
