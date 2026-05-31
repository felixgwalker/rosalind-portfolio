# Strings and Lists (INI3)
# Rosalind problem: https://rosalind.info/problems/ini3/
#
# Problem: Given a string s of length at most 200, and four integers a b c d
# (0-indexed), print the substrings s[a:b] and s[c:d] separated by a space.
#
# Input format:
#   Line 1: the string s
#   Line 2: four integers a b c d

import sys

lines = sys.stdin.read().strip().splitlines()
s = lines[0]
a, b, c, d = map(int, lines[1].split())

# Python slice s[a:b] returns characters at indices a, a+1, ..., b-1
print(s[a:b], s[c:d])
