# Distances in Trees (NKEW) — Newick Format with Branch Lengths
# Rosalind problem: https://rosalind.info/problems/nkew/
#
# Problem: Same as NWCK but branch lengths are given. Compute the sum of branch
# lengths on the path between two leaf nodes in a Newick tree.
#
# Example: (cat:0.1,(dog:0.2,mouse:0.3)carnivore:0.4)mammal;
# Distance(cat, dog) = 0.1 + 0.4 + 0.2 = 0.7

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_nkew.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_newick_weighted(s):
    """Parse a Newick string with branch lengths. Returns weighted adj list."""
    s = s.strip().rstrip(';')
    adj = defaultdict(list)   # node -> [(neighbour, weight)]
    counter = [0]

    def new_node():
        counter[0] += 1
        return f"__node{counter[0]}"

    def parse(pos):
        if s[pos] == '(':
            pos += 1   # skip '('
            children = []
            while True:
                child, weight, pos = parse_with_weight(pos)
                children.append((child, weight))
                if pos < len(s) and s[pos] == ',':
                    pos += 1
                else:
                    break
            pos += 1  # skip ')'
            # Read optional label
            label_start = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[label_start:pos].strip() or new_node()
            for child, weight in children:
                adj[label].append((child, weight))
                adj[child].append((label, weight))
            return label, pos
        else:
            label_start = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            return s[label_start:pos].strip(), pos

    def parse_with_weight(pos):
        node, pos = parse(pos)
        weight = 0.0
        if pos < len(s) and s[pos] == ':':
            pos += 1
            w_start = pos
            while pos < len(s) and s[pos] not in '(),;':
                pos += 1
            weight = float(s[w_start:pos])
        return node, weight, pos

    parse(0)
    return adj

def weighted_bfs(adj, start, end):
    if start == end:
        return 0.0
    visited = {start}
    queue = deque([(start, 0.0)])
    while queue:
        node, dist = queue.popleft()
        for neighbour, weight in adj[node]:
            new_dist = dist + weight
            if neighbour == end:
                return new_dist
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, new_dist))
    return -1.0

def solve(data):
    blocks = data.strip().split('\n\n')
    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue
        newick = lines[0].strip()
        leaf_pair = lines[1].strip().split()
        leaf1, leaf2 = leaf_pair[0], leaf_pair[1]
        adj = parse_newick_weighted(newick)
        print(weighted_bfs(adj, leaf1, leaf2))

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
