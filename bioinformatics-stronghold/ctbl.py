# Creating a Character Table from Leaves (CTBL)
# Rosalind problem: https://rosalind.info/problems/ctbl/
#
# Problem: Given an unrooted tree in Newick format where leaves are labelled,
# output the character table — for each internal edge, the bipartition of leaf
# labels induced by removing that edge. Output as binary strings over sorted
# leaf labels.
#
# Algorithm:
#   1. Parse Newick to get an undirected tree.
#   2. For each internal edge (u, v): remove it and find which leaves are in
#      each component. Output as a binary string (0 = one side, 1 = other).
#   3. Skip edges incident to leaves (leaf edges don't define non-trivial splits).

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_ctbl.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_newick_simple(s):
    """Return (adj, leaves) from Newick string."""
    s = s.strip().rstrip(';')
    adj = defaultdict(list)
    counter = [0]

    def new_node():
        counter[0] += 1
        return f"__n{counter[0]}"

    def parse(pos):
        if pos < len(s) and s[pos] == '(':
            pos += 1
            children = []
            while True:
                child, pos = parse(pos)
                children.append(child)
                if pos < len(s) and s[pos] == ',':
                    pos += 1
                else:
                    break
            pos += 1  # ')'
            label_start = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[label_start:pos].strip() or new_node()
            if pos < len(s) and s[pos] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            for child in children:
                adj[label].append(child)
                adj[child].append(label)
            return label, pos
        else:
            label_start = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[label_start:pos].strip()
            if pos < len(s) and s[pos] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            return label, pos

    parse(0)
    leaves = [n for n in adj if not n.startswith('__n') and len(adj[n]) == 1]
    return adj, sorted(leaves)

def leaves_reachable(adj, start, blocked):
    """BFS from start without crossing the edge (start, blocked)."""
    visited = {start}
    queue = deque([start])
    result = set()
    while queue:
        node = queue.popleft()
        if not node.startswith('__n'):
            result.add(node)
        for nb in adj[node]:
            if nb != blocked and nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return result

def solve(data):
    adj, leaves = parse_newick_simple(data)
    all_leaves = set(leaves)
    seen = set()

    for u in list(adj.keys()):
        for v in adj[u]:
            # Only process each edge once
            if (v, u) in seen:
                continue
            seen.add((u, v))
            # Skip leaf edges (internal bipartitions only)
            if len(adj[u]) == 1 or len(adj[v]) == 1:
                continue
            side0 = leaves_reachable(adj, u, v) & all_leaves
            side1 = all_leaves - side0
            if not side0 or not side1:
                continue
            bits = ''.join('0' if leaf in side0 else '1' for leaf in leaves)
            complement = ''.join('1' if b == '0' else '0' for b in bits)
            print(min(bits, complement))

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
