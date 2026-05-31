# Dictionaries (INI6)
# Rosalind problem: https://rosalind.info/problems/ini6/
#
# Problem: Given a string of space-separated words, count how many times each
# distinct word appears and print "word count" pairs — one per line.
#
# Algorithm: Build a frequency dictionary in a single pass, then print all
# key-value pairs. Order of output does not matter for Rosalind.

import sys

text = sys.stdin.read().strip()
count = {}

for word in text.split():        # split() handles any whitespace, including newlines
    if word in count:
        count[word] += 1
    else:
        count[word] = 1          # first occurrence initialised to 1

for word, freq in count.items():
    print(word, freq)
