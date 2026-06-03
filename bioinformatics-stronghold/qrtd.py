# Quartet Distance (QRTD)
# Rosalind problem: https://rosalind.info/problems/qrtd/
#
# Problem: Given two unrooted binary trees on the same n taxa, compute the
# quartet distance — the number of 4-element subsets of taxa for which the
# two trees induce different quartet topologies.
#
# Algorithm: For each 4-subset of taxa, compute the induced quartet topology
# in both trees and count mismatches.  O(n^4) — suitable for small n.

import os
import sys
from itertools import combinations
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_qrtd.txt')
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

def quartet_topology(adj, a, b, c, d):
    """Return canonical quartet string like 'ab|cd' or None."""
    leaf_set = frozenset([a, b, c, d])
    seen = set()
    for u in list(adj):
        for v in list(adj[u]):
            e = tuple(sorted([u, v], key=str))
            if e in seen:
                continue
            seen.add(e)
            side = set()
            stack = [u]
            while stack:
                node = stack.pop()
                if node in side:
                    continue
                side.add(node)
                for nbr in adj[node]:
                    if nbr != v and nbr not in side:
                        stack.append(nbr)
            sl = sorted(leaf_set & side)
            rl = sorted(leaf_set - side)
            if len(sl) == 2:
                return f'{sl[0]}{sl[1]}|{rl[0]}{rl[1]}'
    return None

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    adj1 = parse_newick(lines[0])
    adj2 = parse_newick(lines[1])
    taxa = sorted(v for v in adj1 if len(adj1[v]) == 1)

    diff = 0
    for a, b, c, d in combinations(taxa, 4):
        t1 = quartet_topology(adj1, a, b, c, d)
        t2 = quartet_topology(adj2, a, b, c, d)
        if t1 != t2:
            diff += 1

    print(diff)

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
