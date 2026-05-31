# Variables and Some Arithmetic (INI2)
# Rosalind problem: https://rosalind.info/problems/ini2/
#
# Problem: Given two positive integers a and b (each ≤ 1000), print the
# sum of their squares: a² + b².
#
# Input format: two integers on separate lines (or space-separated).

import sys

data = sys.stdin.read().split()
a, b = int(data[0]), int(data[1])

# The sum of squares: straightforward arithmetic
print(a**2 + b**2)
