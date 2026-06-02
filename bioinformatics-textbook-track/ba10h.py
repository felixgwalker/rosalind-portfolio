# BA10H — Estimate the Parameters of an HMM
# https://rosalind.info/problems/ba10h/
#
# Given: emitted string x and hidden path π, alphabet, states.
# Return: estimated transition and emission matrices (MLE from counts).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba10h.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    x = lines[0].strip(); path = lines[2].strip()
    alphabet = lines[4].strip().split(); states = lines[6].strip().split()
    # Count transitions
    trans_count = defaultdict(lambda: defaultdict(int))
    for i in range(len(path)-1):
        trans_count[path[i]][path[i+1]] += 1
    # Count emissions
    emit_count = defaultdict(lambda: defaultdict(int))
    for xi, si in zip(x, path):
        emit_count[si][xi] += 1
    # Normalize
    print('\t'.join([''] + states))
    for s in states:
        total = sum(trans_count[s].values())
        row = [f"{trans_count[s][t]/total:.3f}" if total>0 else "0.000" for t in states]
        print('\t'.join([s] + row))
    print('--------')
    print('\t'.join([''] + alphabet))
    for s in states:
        total = sum(emit_count[s].values())
        row = [f"{emit_count[s][a]/total:.3f}" if total>0 else "0.000" for a in alphabet]
        print('\t'.join([s] + row))

if __name__ == '__main__': solve(get_input())
