# BA9P — Implement TreeColoring
# https://rosalind.info/problems/ba9p/
#
# Given: A rooted tree and a coloring of its leaves (blue=0, red=1, gray=-).
# Return: A coloring of all nodes such that each internal node is colored
#         reddish (1) if all colored descendants are red, bluish (0) if all
#         colored descendants are blue, or gray (-) if the subtree contains
#         both colors.
#
# This tree-coloring primitive underlies the multiple approximate pattern
# matching algorithm in the textbook (Chapter 9).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9p.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    # Parse: first line is the number of nodes, then each remaining line is
    # "node -> child1 child2 ..." or just leaf colorings at the end.
    # Format: edges first, then one line per node giving its initial color.
    # We detect the format from the data.

    # Expected input format:
    #   Line 1: number of nodes n
    #   Next lines: "parent -> child" edges
    #   Then: "node: color" color assignments (0, 1, or -)
    children = defaultdict(list)
    parent = {}
    color = {}

    idx = 0
    n = int(lines[idx]); idx += 1
    # Edges
    while idx < len(lines) and '->' in lines[idx]:
        parts = lines[idx].split('->')
        p_node = int(parts[0].strip())
        for ch in parts[1].strip().split():
            c = int(ch)
            children[p_node].append(c)
            parent[c] = p_node
        idx += 1
    # Colors
    while idx < len(lines) and lines[idx].strip():
        parts = lines[idx].split(':')
        node = int(parts[0].strip())
        col = parts[1].strip()
        color[node] = int(col) if col != '-' else -1
        idx += 1

    # Find root (no parent)
    all_nodes = set(range(1, n + 1))
    roots = all_nodes - set(parent.keys())
    root = min(roots)

    def dfs(node):
        if node not in children or not children[node]:
            return color.get(node, -1)
        child_colors = [dfs(c) for c in children[node]]
        non_gray = [c for c in child_colors if c != -1]
        if not non_gray:
            color[node] = -1
        elif all(c == 1 for c in non_gray):
            color[node] = 1
        elif all(c == 0 for c in non_gray):
            color[node] = 0
        else:
            color[node] = -1
        return color[node]

    dfs(root)

    for node in sorted(all_nodes):
        c = color.get(node, -1)
        print(f"{node}: {c if c != -1 else '-'}")

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
