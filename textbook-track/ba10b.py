# BA10B — Compute the Probability of an Outcome Given a Hidden Path
# https://rosalind.info/problems/ba10b/
#
# Given: a string x, alphabet Σ, hidden path π, states, and emission matrix.
# Return: the probability P(x|π).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba10b.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    x = lines[0].strip()
    alphabet = lines[2].strip().split()
    path = lines[4].strip()
    states = lines[6].strip().split()
    emit = {}
    for line in lines[8:]:
        if not line.strip(): break
        parts = line.split()
        emit[parts[0]] = {alphabet[i]: float(parts[i+1]) for i in range(len(alphabet))}
    prob = 1.0
    for ch, st in zip(x, path):
        prob *= emit[st][ch]
    print(f"{prob:.2e}")

if __name__ == '__main__': solve(get_input())
