# Completing a Tree (TREE)
# Rosalind problem: https://rosalind.info/problems/tree/
#
# Problem: Given n nodes and a list of edges forming a forest (acyclic graph),
# return the minimum number of edges needed to convert the forest into a tree
# (a connected acyclic graph on n nodes).
#
# Key fact: A tree on n nodes has exactly n-1 edges. If the current forest has
# e edges and c connected components, then c = n - e, and we need c - 1 more
# edges to connect all components into one tree.
#
# Algorithm: Union-Find (disjoint set union) to count connected components. O(n·α(n)).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_tree.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())

    # Union-Find with path compression
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path compression
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    for line in lines[1:]:
        line = line.strip()
        if line:
            a, b = map(int, line.split())
            union(a, b)

    # Count distinct roots (connected components) among nodes 1..n
    components = len({find(i) for i in range(1, n + 1)})
    print(components - 1)   # edges needed to connect all components

if __name__ == '__main__':
    solve(get_input())
