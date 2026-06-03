# Quartets (QRT)
# Rosalind problem: https://rosalind.info/problems/qrt/
#
# Problem: Given two unrooted binary trees T1 and T2 on the same n taxa,
# output the set of quartets that are consistent with BOTH trees.
# A quartet ab|cd means leaves a,b are on one side of the separating edge
# and c,d are on the other.
#
# Algorithm: For each 4-element subset of taxa, determine the induced quartet
# topology in T1 and T2 by finding the unique internal edge whose removal
# separates the 4 leaves 2-and-2.  Output any quartet consistent in both.
#
# O(n^4) — feasible for n ≤ a few dozen.

import os
import sys
from itertools import combinations
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_qrt.txt')
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

def leaves_of(adj):
    return [v for v in adj if len(adj[v]) == 1]

def quartet_topology(adj, a, b, c, d):
    """Return one of ('ab|cd','ac|bd','ad|bc') or None if unresolved."""
    leaf_set = frozenset([a, b, c, d])
    # Try each edge; check if it separates exactly 2 leaves on each side
    seen = set()
    for u in adj:
        for v in adj[u]:
            e = tuple(sorted([u, v], key=str))
            if e in seen:
                continue
            seen.add(e)
            # BFS side containing u (excluding v)
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
            side_leaves = leaf_set & side
            if len(side_leaves) == 2:
                sl = sorted(side_leaves)
                rl = sorted(leaf_set - side_leaves)
                return f'{sl[0]}{sl[1]}|{rl[0]}{rl[1]}'
    return None

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    adj1 = parse_newick(lines[0])
    adj2 = parse_newick(lines[1])
    taxa = sorted(leaves_of(adj1))

    common = []
    for a, b, c, d in combinations(taxa, 4):
        t1 = quartet_topology(adj1, a, b, c, d)
        t2 = quartet_topology(adj2, a, b, c, d)
        if t1 and t2 and t1 == t2:
            common.append(t1)

    for q in sorted(common):
        print(q)

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
