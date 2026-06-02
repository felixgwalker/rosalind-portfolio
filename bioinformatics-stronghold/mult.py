# Multiple Alignment (MULT)
# Rosalind problem: https://rosalind.info/problems/mult/
#
# Problem: Given at most 5 DNA strings each of length ≤ 10, find the
# highest-scoring multiple sequence alignment using sum-of-pairs scoring:
#   • both letters match  → +1 per pair
#   • letters differ       → -1 per pair
#   • one letter, one gap  → -1 per pair
#   • gap vs gap           →  0 per pair
#
# Algorithm: DP over a k-dimensional table (k ≤ 5, each dimension ≤ 11).
#   State (i₁,…,iₖ) = characters consumed in each string.
#   Transition: choose any non-empty subset S of strings to advance by 1;
#   strings not in S contribute a gap column.  Score the column via all pairs.
#   Traceback with recursive memoised DP.

import os
import sys
from functools import lru_cache

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_mult.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def solve(data):
    strings = [l.strip() for l in data.splitlines() if l.strip() and not l.startswith('>')]
    k = len(strings)
    lens = tuple(len(s) for s in strings)
    subsets = list(range(1, 1 << k))  # all non-empty subsets

    def col_score(state, mask):
        sc = 0
        for a in range(k):
            for b in range(a + 1, k):
                a_in = bool((mask >> a) & 1)
                b_in = bool((mask >> b) & 1)
                if a_in and b_in:
                    sc += 1 if strings[a][state[a]] == strings[b][state[b]] else -1
                elif a_in or b_in:
                    sc -= 1
        return sc

    @lru_cache(maxsize=None)
    def dp(state):
        if state == lens:
            return 0
        best = float('-inf')
        for mask in subsets:
            new = list(state)
            ok = True
            for j in range(k):
                if (mask >> j) & 1:
                    if state[j] >= lens[j]:
                        ok = False
                        break
                    new[j] += 1
            if not ok:
                continue
            val = col_score(state, mask) + dp(tuple(new))
            if val > best:
                best = val
        return best

    def traceback(state):
        if state == lens:
            return [''] * k
        target = dp(state)
        for mask in subsets:
            new = list(state)
            ok = True
            for j in range(k):
                if (mask >> j) & 1:
                    if state[j] >= lens[j]:
                        ok = False
                        break
                    new[j] += 1
            if not ok:
                continue
            if col_score(state, mask) + dp(tuple(new)) == target:
                sub = traceback(tuple(new))
                return [
                    (strings[j][state[j]] if (mask >> j) & 1 else '-') + sub[j]
                    for j in range(k)
                ]
        return [''] * k  # unreachable for valid input

    init = tuple(0 for _ in range(k))
    print(dp(init))
    for row in traceback(init):
        print(row)

if __name__ == '__main__':
    solve(get_input())
