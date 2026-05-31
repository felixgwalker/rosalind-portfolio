# Matching Random Motifs (RSTR)
# Rosalind problem: https://rosalind.info/problems/rstr/
#
# Problem: Given N (number of random strings to generate), a GC content x,
# and a DNA string s, compute the probability that at least one of N random
# strings of the same length as s equals s exactly.
#
# Model: Under GC content x, each position is independently drawn with
#   P(G) = P(C) = x/2,  P(A) = P(T) = (1-x)/2.
#
# Formula:
#   P(single random string == s) = product of per-base probs = p_s
#   P(at least one of N equals s) = 1 - (1 - p_s)^N

import os
import sys
import math

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_rstr.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    N, x = lines[0].split()
    N = int(N)
    x = float(x)
    s = lines[1].strip()

    # Probability that one random string equals s
    log_p = 0.0
    for base in s:
        if base in 'GC':
            log_p += math.log(x / 2)
        else:
            log_p += math.log((1 - x) / 2)
    p_s = math.exp(log_p)

    # P(at least one match) = 1 - P(no match in N draws)
    result = 1 - (1 - p_s) ** N
    print(round(result, 3))

if __name__ == '__main__':
    solve(get_input())
