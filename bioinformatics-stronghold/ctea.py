# Counting Topological Orderings of Evolutionary Ancestors (CTEA)
# Rosalind problem: https://rosalind.info/problems/ctea/
#
# Problem: Given a rooted binary tree (Newick), count the number of ways to
# order its internal (non-leaf) nodes such that every ancestor appears before
# every one of its descendants (i.e., count linear extensions of the partial
# order defined by the tree).
#
# Formula (hook-length for trees):
#   count = m! / ∏_{v internal} size_internal(v)
# where m = total number of internal nodes and size_internal(v) is the count
# of internal nodes in the subtree rooted at v (including v itself).
#
# Return the count modulo 1,000,000.

import os
import sys
import math

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_ctea.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_newick(s):
    s = s.strip().rstrip(';')
    children = {}
    counter = [0]

    def new_node():
        counter[0] += 1
        return f'__n{counter[0]}'

    def parse(pos):
        if pos < len(s) and s[pos] == '(':
            pos += 1
            kids = []
            while True:
                child, pos = parse(pos)
                kids.append(child)
                if pos < len(s) and s[pos] == ',':
                    pos += 1
                else:
                    break
            pos += 1
            lb = pos
            while pos < len(s) and s[pos] not in '(),;':
                pos += 1
            label = s[lb:pos].strip() or new_node()
            children[label] = kids
            return label, pos
        else:
            lb = pos
            while pos < len(s) and s[pos] not in '(),;':
                pos += 1
            label = s[lb:pos].strip()
            children.setdefault(label, [])
            return label, pos

    root, _ = parse(0)
    return root, children

def solve(data):
    root, children = parse_newick(data.strip())

    # Compute internal-node subtree sizes
    int_size = {}

    def compute_size(v):
        if not children[v]:
            int_size[v] = 0  # leaf contributes 0 internal nodes
            return 0
        total = 1  # v itself is an internal node
        for c in children[v]:
            total += compute_size(c)
        int_size[v] = total
        return total

    compute_size(root)

    internals = [v for v in int_size if int_size[v] > 0 or children[v]]
    # Re-filter: internal nodes are those with children
    internals = [v for v in children if children[v]]
    m = len(internals)

    # count = m! / product of int_size[v] for all internal v
    numerator = math.factorial(m)
    denominator = 1
    for v in internals:
        denominator *= int_size[v]

    result = (numerator // denominator) % 1_000_000
    print(result)

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
