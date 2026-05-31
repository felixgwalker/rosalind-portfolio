# Enumerating Gene Orders (PERM)
# Rosalind problem: https://rosalind.info/problems/perm/
#
# Problem: Given a positive integer n (≤ 7), output n! (the total number of
# permutations) followed by all permutations of the set {1, 2, ..., n},
# one permutation per line with elements space-separated.
#
# Algorithm: Heap's algorithm (or itertools) for generating all permutations
# in lexicographic order via a recursive backtracking approach. O(n! · n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_perm.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def permutations(items):
    """Generate all permutations of items using recursive backtracking."""
    if len(items) <= 1:
        yield list(items)
        return
    for i, item in enumerate(items):
        rest = items[:i] + items[i+1:]
        for perm in permutations(rest):
            yield [item] + perm

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def solve(data):
    n = int(data.strip())
    items = list(range(1, n + 1))
    perms = list(permutations(items))
    print(factorial(n))
    for p in perms:
        print(' '.join(map(str, p)))

if __name__ == '__main__':
    solve(get_input())
