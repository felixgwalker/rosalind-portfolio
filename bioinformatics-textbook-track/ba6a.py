# BA6A — Implement GreedySorting to Sort a Permutation by Reversals
# https://rosalind.info/problems/ba6a/
#
# Given: a signed permutation P.
# Return: each intermediate permutation after applying GreedySorting steps.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba6a.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def reverse_segment(perm, i, j):
    perm[i:j+1] = [-x for x in reversed(perm[i:j+1])]

def fmt(perm):
    return '(' + ' '.join((f'+{x}' if x>0 else str(x)) for x in perm) + ')'

def greedy_sort(perm):
    steps, n = [], len(perm)
    for k in range(n):
        if perm[k] == k+1: continue
        # Find k+1 or -(k+1) at position j >= k
        j = next(i for i in range(k, n) if abs(perm[i]) == k+1)
        reverse_segment(perm, k, j)
        steps.append(fmt(perm))
        if perm[k] < 0:
            perm[k] = -perm[k]
            steps.append(fmt(perm))
    return steps

def solve(data):
    perm = list(map(int, data.strip().strip('()').split()))
    steps = greedy_sort(perm)
    print('\n'.join(steps))

if __name__ == '__main__': solve(get_input())
