# Maximal Independent Set (MIS)
# Rosalind problem: https://rosalind.info/problems/mis/
#
# Problem: Given a simple graph, find a maximum-weight independent set — a set
# of nodes with no adjacent pair, maximising the total weight.
# For general graphs this is NP-hard; Rosalind uses path graphs (or trees)
# where it can be solved with DP in O(n).
#
# For a path graph with weights w[1..n]:
#   dp[i] = max weight independent set of nodes 1..i
#   dp[i] = max(dp[i-1], dp[i-2] + w[i])
# Output: the subset of selected nodes.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_mis.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n = int(lines[0])
    weights = list(map(int, lines[1].split()))

    # DP for maximum weight independent set on a path
    dp = [0] * (n + 1)
    dp[1] = weights[0]
    if n > 1:
        dp[2] = max(weights[0], weights[1])

    for i in range(3, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + weights[i-1])

    # Backtrack to find which nodes are selected
    selected = []
    i = n
    while i >= 1:
        if i == 1 or dp[i] != dp[i-1]:
            selected.append(i)
            i -= 2
        else:
            i -= 1

    # Output as a binary string: 1 = included, 0 = excluded
    result = ['0'] * n
    for idx in selected:
        result[idx - 1] = '1'
    print(''.join(result))

if __name__ == '__main__':
    solve(get_input())
