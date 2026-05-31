# Expected Number of Restriction Sites (EVAL)
# Rosalind problem: https://rosalind.info/problems/eval/
#
# Problem: Given a positive integer n (length of random genome), a DNA string s
# (restriction site pattern), and an array A of GC content values, for each
# x in A compute the expected number of times s appears as a substring in a
# random genome of length n with GC content x.
#
# Formula:
#   E[occurrences of s] = (n - |s| + 1) × P(s | x)
# where P(s | x) = product of per-base probabilities (same model as PROB/RSTR).
#   P(G or C) = x/2,  P(A or T) = (1-x)/2

import os
import sys
import math

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_eval.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    s = lines[1].strip()
    gc_values = list(map(float, lines[2].split()))

    positions = n - len(s) + 1   # number of starting positions

    results = []
    for x in gc_values:
        log_p = 0.0
        for base in s:
            if base in 'GC':
                log_p += math.log(x / 2)
            else:
                log_p += math.log((1 - x) / 2)
        p_s = math.exp(log_p)
        expected = positions * p_s
        results.append(round(expected, 6))

    print(' '.join(map(str, results)))

if __name__ == '__main__':
    solve(get_input())
