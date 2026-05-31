# Conditions and Loops (INI4)
# Rosalind problem: https://rosalind.info/problems/ini4/
#
# Problem: Given two positive integers a and b (a < b < 10000), sum all
# odd integers in the closed interval [a, b].
#
# Algorithm: Iterate from a to b inclusive, accumulate when i % 2 != 0.

import sys

data = sys.stdin.read().split()
a, b = int(data[0]), int(data[1])

total = 0
for x in range(a, b + 1):
    if x % 2 != 0:   # odd numbers only
        total += x

print(total)
