# Introduction to Pattern Matching (TRIE)
# Rosalind problem: https://rosalind.info/problems/trie/
#
# Problem: Given a list of DNA strings, construct a trie (prefix tree) from
# them. Output the edges of the trie, each as "node1 node2 label" where node1
# is the parent, node2 is the child, and label is the single character on the edge.
# Nodes are numbered starting from 1 (root = 1).
#
# Algorithm: Insert each string character by character into the trie, creating
# new nodes as needed. O(Σ |s_i|) total time.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_trie.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    strings = [line.strip() for line in data.splitlines() if line.strip()]

    # Each trie node is a dict: char -> child_node_id
    # nodes[i] = children dict of node i (1-indexed, root = 1)
    nodes = [{}]      # nodes[0] is unused; nodes[1] = root = {}
    nodes.append({})  # nodes[1] = root

    edges = []
    node_count = 1   # root is node 1

    for s in strings:
        current = 1   # start at root
        for ch in s:
            if ch not in nodes[current]:
                # Create new child node
                node_count += 1
                nodes.append({})
                nodes[current][ch] = node_count
                edges.append((current, node_count, ch))
            current = nodes[current][ch]

    for parent, child, label in edges:
        print(parent, child, label)

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
