# BA9Q — Construct the Partial Suffix Array of a String
# https://rosalind.info/problems/ba9q/
#
# Given: A string Text and a positive integer K.
# Return: SuffixArrayK(Text), the partial suffix array of Text with step K.
#         Only output pairs (i, SA[i]) where SA[i] mod K = 0.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9q.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    text = lines[0].strip()
    K = int(lines[1].strip())
    if not text.endswith('$'):
        text += '$'
    n = len(text)
    sa = sorted(range(n), key=lambda i: text[i:])
    for i, s in enumerate(sa):
        if s % K == 0:
            print(f"{i}: {s}")

if __name__ == '__main__': solve(get_input())
