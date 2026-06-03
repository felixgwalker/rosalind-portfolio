# Enumerating Unrooted Binary Trees (EUBT)
# Rosalind problem: https://rosalind.info/problems/eubt/
#
# Problem: Given a positive integer n (and optionally n taxon labels), output
# all distinct unrooted binary trees on n labeled leaves in Newick format,
# one per line.
#
# Algorithm: iterative leaf insertion.
#   • Start with the unique 3-leaf star represented as an adjacency dict.
#   • For each new leaf from 4 to n: for every existing tree and every edge
#     in that tree, create a new tree by subdividing the edge with a new
#     internal node connected to the new leaf.
#   • Each tree is stored as a frozenset of frozenset-pairs (its split set)
#     for deduplication; Newick is generated on output.

import os
import sys
from copy import deepcopy

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_eubt.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

# --- Tree representation: adjacency dict {node: set of neighbours} ---
# Leaf nodes are ints (1-based); internal nodes are negative ints.

_int_counter = [0]

def new_internal():
    _int_counter[0] -= 1
    return _int_counter[0]

def get_edges(adj):
    edges = set()
    for u, nbrs in adj.items():
        for v in nbrs:
            if u < v or (isinstance(u, int) and isinstance(v, str)) or \
               (isinstance(u, str) and isinstance(v, int)):
                edges.add((min(str(u), str(v)), max(str(u), str(v))))
    return [(u, v) for u, v in edges]

def tree_edges(adj):
    seen = set()
    result = []
    for u in adj:
        for v in adj[u]:
            e = tuple(sorted([u, v], key=str))
            if e not in seen:
                seen.add(e)
                result.append(e)
    return result

def insert_leaf(adj, edge, new_leaf):
    """Return new adjacency dict with new_leaf inserted on edge (u,v)."""
    u, v = edge
    w = ('_i', id(adj), u, v)  # unique internal node key
    new_adj = {node: set(nbrs) for node, nbrs in adj.items()}
    # Remove old edge
    new_adj[u].discard(v); new_adj[v].discard(u)
    # Add new internal node w connected to u, v, new_leaf
    new_adj[w] = {u, v, new_leaf}
    new_adj[u].add(w); new_adj[v].add(w)
    new_adj[new_leaf] = {w}
    return new_adj

def canonical_splits(adj, leaves):
    """Frozenset of frozenset-pairs representing all non-trivial splits."""
    leaf_set = frozenset(leaves)
    splits = set()
    for u, v in tree_edges(adj):
        # BFS from u not crossing (u,v) → get one side
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
        l_leaves = frozenset(x for x in side if x in leaf_set)
        r_leaves = leaf_set - l_leaves
        if len(l_leaves) >= 2 and len(r_leaves) >= 2:
            splits.add(frozenset([l_leaves, r_leaves]))
    return frozenset(splits)

def to_newick(adj, node, parent, leaves):
    children = [n for n in adj[node] if n != parent]
    if not children:
        return str(node)
    return '(' + ','.join(sorted(to_newick(adj, c, node, leaves) for c in children)) + ')'

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    n = int(lines[0])
    labels = list(range(1, n + 1))
    if len(lines) > 1:
        # Taxa labels provided
        labels = lines[1].split()
        n = len(labels)

    if n == 1:
        print(str(labels[0]))
        return
    if n == 2:
        print(f'({labels[0]},{labels[1]})')
        return

    # Start with the unique 3-leaf star
    l1, l2, l3 = labels[0], labels[1], labels[2]
    root_int = ('_i', 0)
    init_adj = {
        l1: {root_int}, l2: {root_int}, l3: {root_int},
        root_int: {l1, l2, l3}
    }
    trees = {canonical_splits(init_adj, [l1, l2, l3]): init_adj}

    for idx in range(3, n):
        new_leaf = labels[idx]
        new_trees = {}
        for splits, adj in trees.items():
            for edge in tree_edges(adj):
                new_adj = insert_leaf(adj, edge, new_leaf)
                cs = canonical_splits(new_adj, labels[:idx+1])
                if cs not in new_trees:
                    new_trees[cs] = new_adj
        trees = new_trees

    for adj in sorted(trees.values(), key=lambda a: str(sorted(str(k) for k in a))):
        # Root the Newick at leaf labels[0]
        l0 = labels[0]
        internal_root = next(iter(adj[l0]))
        # Output trifurcating form rooted at the internal node adjacent to labels[0]
        children = [n for n in adj[internal_root] if n != l0]
        if len(children) == 2:
            c1, c2 = children
            t1 = to_newick(adj, c1, internal_root, labels)
            t2 = to_newick(adj, c2, internal_root, labels)
            print(f'({labels[0]},{t1},{t2})')
        else:
            parts = [to_newick(adj, c, internal_root, labels) for c in children]
            print(f'({labels[0]},' + ','.join(sorted(parts)) + ')')

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
