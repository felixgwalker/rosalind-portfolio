# BA9F — Find the Shortest Non-Shared Substring of Two Strings
# https://rosalind.info/problems/ba9f/
#
# Given: two strings s and t. Return: the shortest substring of s that does not appear in t.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9f.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    s, t = lines[0].strip(), lines[1].strip()
    # Binary search on length, then check
    for length in range(1, len(s)+1):
        for i in range(len(s)-length+1):
            sub = s[i:i+length]
            if sub not in t:
                print(sub); return

if __name__ == '__main__': solve(get_input())
