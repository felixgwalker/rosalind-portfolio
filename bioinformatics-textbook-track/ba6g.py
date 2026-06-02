# BA6G — Implement CycleToChromosome
# https://rosalind.info/problems/ba6g/
#
# Given: a sequence of nodes forming a cycle.
# Return: the corresponding chromosome (signed permutation).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba6g.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    nodes = list(map(int, data.strip().strip('()').split()))
    chromosome = []
    for i in range(0, len(nodes), 2):
        t, h = nodes[i], nodes[i+1]
        if h == t + 1:   # positive element: t = 2x-1, h = 2x → x = h/2
            chromosome.append(h // 2)
        else:            # negative element: h = 2x-1, t = 2x → x = t/2 (negative)
            chromosome.append(-(t // 2))
    print('(' + ' '.join(map(str, chromosome)) + ')')

if __name__ == '__main__': solve(get_input())
