# Finding the Longest Multiple Repeat (LREP)
# Rosalind problem: https://rosalind.info/problems/lrep/
#
# Problem: Given a DNA string s (terminated with '$') and an integer k, plus
# the suffix tree of s given explicitly as a list of edges
# "parent child edge_start edge_length" (1-indexed positions into s), find the
# longest substring of s that occurs at least k times.
#
# Algorithm: Walk the suffix tree.
#   For any node v, the path-label from the root to v is a substring of s that
#   occurs exactly len(leaves(v)) times (one occurrence per suffix passing
#   through v), and that count is constant along the whole edge into v (suffix
#   tree internal nodes only sit at branch points). So the answer is the
#   path-label of the deepest node whose leaf count is >= k. Leaf counts are
#   computed bottom-up; the longest qualifying path-label is then rebuilt by
#   walking parent links back to the root.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_lrep.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read(), None

def solve(data):
    lines = data.strip('\n').splitlines()
    s = lines[0].strip()
    k = int(lines[1].strip())

    children = defaultdict(list)   # node -> [(child, edge_start, edge_length), ...]
    parent_of = {}
    edge_label = {}                # node -> (edge_start, edge_length) of edge from its parent
    child_nodes = set()

    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue
        parent, child, start, length = line.split()
        start, length = int(start), int(length)
        children[parent].append((child, start, length))
        parent_of[child] = parent
        edge_label[child] = (start, length)
        child_nodes.add(child)

    all_nodes = set(children.keys()) | child_nodes
    root = next(node for node in all_nodes if node not in child_nodes)

    # BFS from root: string-depth of each node and a processing order for the
    # later bottom-up leaf-count pass (reverse of this order is bottom-up).
    depth = {root: 0}
    order = [root]
    queue = [root]
    while queue:
        node = queue.pop()
        for child, _start, length in children.get(node, []):
            depth[child] = depth[node] + length
            order.append(child)
            queue.append(child)

    leaf_count = {}
    for node in reversed(order):
        kids = children.get(node, [])
        leaf_count[node] = 1 if not kids else sum(leaf_count[c] for c, _, _ in kids)

    best_node, best_depth = None, -1
    for node in all_nodes:
        if node != root and leaf_count[node] >= k and depth[node] > best_depth:
            best_node, best_depth = node, depth[node]

    path = []
    node = best_node
    while node != root:
        path.append(edge_label[node])
        node = parent_of[node]
    path.reverse()

    substring = ''.join(s[start - 1:start - 1 + length] for start, length in path)
    substring = substring.rstrip('$')   # '$' is the suffix-tree terminator, not part of s

    print(substring)

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
