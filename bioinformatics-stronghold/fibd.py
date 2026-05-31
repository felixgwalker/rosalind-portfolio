# Mortal Fibonacci Rabbits (FIBD)
# Rosalind problem: https://rosalind.info/problems/fibd/
#
# Problem: Like the standard Fibonacci rabbit model but each pair of rabbits
# dies after m months. Given n (months, ≤ 100) and m (lifespan, ≤ 20), return
# the number of rabbit pairs alive at the end of month n.
#
# Algorithm: Track a cohort array where cohort[i] = pairs that are i months old.
#   Each month:
#     new_babies = sum of all mature pairs (age ≥ 1) = sum(cohort[1:])
#     Shift everyone one month older (oldest cohort dies by falling off the end)
#     cohort[0] = new_babies
# O(n·m) time, O(m) space.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_fibd.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    n, m = map(int, data.split())

    # cohort[i] = number of pairs that are exactly i months old
    # (0 = just born, m-1 = oldest alive, they die after this month)
    cohort = [0] * m
    cohort[0] = 1    # initial young pair

    for _ in range(n - 1):
        # Pairs aged 1 to m-1 can reproduce (mature)
        new_babies = sum(cohort[1:])
        # Shift: cohort[m-1] dies, everyone else ages one month
        cohort = [new_babies] + cohort[:-1]

    print(sum(cohort))

if __name__ == '__main__':
    solve(get_input())
