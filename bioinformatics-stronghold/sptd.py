# Phylogeny Comparison with Split Distance (SPTD)
# Rosalind problem: https://rosalind.info/problems/sptd/
#
# Problem: Given two unrooted Newick trees on the same set of n taxa, compute
# the split distance — the size of the symmetric difference of their split sets.
# (Each internal edge of an unrooted tree defines a bipartition of the leaves.)
#
# Algorithm:
#   For each tree, enumerate all non-trivial splits (bipartitions into sets of
#   size ≥ 2) by performing a DFS that identifies the leaf-set on each side of
#   every edge.  Represent each split as a frozenset of two frozensets, then
#   compute |splits(T1) △ splits(T2)|.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_sptd.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def parse_newick_unrooted(s):
    """Parse Newick into undirected adjacency dict.  Leaves are named; internal
    nodes without labels get auto names."""
    s = s.strip().rstrip(';')
    adj = defaultdict(set)
    counter = [0]

    def new_node():
        counter[0] += 1
        return f'__i{counter[0]}'

    def parse(pos):
        if s[pos] == '(':
            pos += 1
            kids = []
            while True:
                child, pos = parse(pos)
                kids.append(child)
                if s[pos] == ',':
                    pos += 1
                else:
                    break
            pos += 1  # ')'
            lb = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[lb:pos].strip() or new_node()
            if s[pos:pos+1] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            for c in kids:
                adj[label].add(c)
                adj[c].add(label)
            return label, pos
        else:
            lb = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[lb:pos].strip()
            if s[pos:pos+1] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            return label, pos

    parse(0)
    return adj

def get_leaves(adj):
    return frozenset(v for v in adj if len(adj[v]) == 1)

def get_splits(adj):
    leaves = get_leaves(adj)
    splits = set()

    def leaf_subtree(node, forbidden):
        """Return frozenset of leaves reachable from node without crossing forbidden."""
        stack, seen = [node], set()
        result = set()
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            if v in leaves:
                result.add(v)
            for nbr in adj[v]:
                if nbr != forbidden and nbr not in seen:
                    stack.append(nbr)
        return frozenset(result)

    seen_edges = set()
    for u in adj:
        for v in adj[u]:
            e = tuple(sorted([u, v]))
            if e in seen_edges:
                continue
            seen_edges.add(e)
            side_u = leaf_subtree(u, v)
            side_v = leaves - side_u
            if len(side_u) >= 2 and len(side_v) >= 2:
                splits.add(frozenset([side_u, side_v]))
    return splits

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    # Two Newick trees, possibly separated by a blank line or just two lines
    results = []
    i = 0
    while i < len(lines):
        t1 = lines[i]; t2 = lines[i+1] if i+1 < len(lines) else ''
        if not t2:
            break
        adj1 = parse_newick_unrooted(t1)
        adj2 = parse_newick_unrooted(t2)
        s1, s2 = get_splits(adj1), get_splits(adj2)
        results.append(len(s1.symmetric_difference(s2)))
        i += 2

    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve(get_input())
