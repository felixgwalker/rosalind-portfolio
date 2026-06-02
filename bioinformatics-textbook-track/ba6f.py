# BA6F — Implement ChromosomeToCycle
# https://rosalind.info/problems/ba6f/
#
# Given: a signed permutation (chromosome).
# Return: the corresponding cycle of nodes.
# For each element x: if x>0: nodes 2x-1, 2x; if x<0: nodes -2x, -2x-1.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba6f.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    perm = list(map(int, data.strip().strip('()').split()))
    nodes = []
    for x in perm:
        if x > 0: nodes.extend([2*x-1, 2*x])
        else: nodes.extend([-2*x, -2*x-1])
    print('(' + ' '.join(map(str, nodes)) + ')')

if __name__ == '__main__': solve(get_input())
