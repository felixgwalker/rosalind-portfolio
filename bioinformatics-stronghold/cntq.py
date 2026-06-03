# Counting Quartets (CNTQ)
# Rosalind problem: https://rosalind.info/problems/cntq/
#
# Problem: Given an unrooted (possibly non-binary) Newick tree on n taxa,
# count the number of resolved quartets — 4-element subsets of leaves for
# which the induced subtree has a definite binary topology (not a star).
#
# Formula: for each internal edge e with leaf sizes L and R on its two sides,
# it contributes C(L,2)×C(R,2) resolved quartets.  Summing over all internal
# edges gives the total (each resolved quartet counted exactly once for the
# deepest edge that separates it).
#
# For a fully binary tree on n leaves this equals C(n,4).

import os
import sys
from math import comb
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_cntq.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_newick(s):
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
            pos += 1
            lb = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[lb:pos].strip() or new_node()
            if s[pos:pos+1] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            for c in kids:
                adj[label].add(c); adj[c].add(label)
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

def count_leaves_side(adj, start, forbidden):
    """Count leaves reachable from start without crossing forbidden."""
    count = 0
    stack, seen = [start], set()
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        if len(adj[v]) == 1:
            count += 1
        for nbr in adj[v]:
            if nbr != forbidden and nbr not in seen:
                stack.append(nbr)
    return count

def solve(data):
    adj = parse_newick(data.strip())
    total_leaves = sum(1 for v in adj if len(adj[v]) == 1)

    seen = set()
    total = 0
    for u in adj:
        for v in adj[u]:
            e = tuple(sorted([u, v], key=str))
            if e in seen:
                continue
            seen.add(e)
            L = count_leaves_side(adj, u, v)
            R = total_leaves - L
            total += comb(L, 2) * comb(R, 2)

    print(total)

if __name__ == '__main__':
    import io, contextlib
    data, out_path = get_input()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        solve(data)
    output = buf.getvalue()
    sys.stdout.write(output)
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(output)
