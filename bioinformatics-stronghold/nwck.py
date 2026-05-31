# Distances in Trees (NWCK)
# Rosalind problem: https://rosalind.info/problems/nwck/
#
# Problem: Given a Newick-format tree and a pair of leaf labels, find the
# edge-count distance between them (number of edges on the unique path).
# Multiple test cases may be given (tree and pair on adjacent lines).
#
# Algorithm: Parse Newick into an adjacency list, then BFS/DFS to find
# the distance between two named nodes.
#
# Newick format (simplified): ((leaf1,leaf2)inner1,(leaf3)inner2)root;
# We parse recursively using a simple tokeniser.

import os
import sys
from collections import defaultdict, deque

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_nwck.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def parse_newick(s):
    """Parse a Newick string into an undirected adjacency list.
    Returns adj: dict of node_name -> list of neighbour names.
    Internal nodes without labels get auto-generated names."""
    s = s.strip().rstrip(';')
    adj = defaultdict(list)
    counter = [0]  # mutable counter for auto-naming internal nodes

    def new_node():
        counter[0] += 1
        return f"__node{counter[0]}"

    def parse(pos):
        """Parse starting at pos; return (node_name, new_pos)."""
        if s[pos] == '(':
            # Internal node: parse children
            internal = None
            pos += 1   # skip '('
            children = []
            while True:
                child, pos = parse(pos)
                children.append(child)
                if s[pos] == ',':
                    pos += 1
                else:
                    break
            pos += 1  # skip ')'
            # Read optional internal node label
            label_start = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[label_start:pos].strip()
            if not label:
                label = new_node()
            # Skip optional branch length
            if pos < len(s) and s[pos] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            for child in children:
                adj[label].append(child)
                adj[child].append(label)
            return label, pos
        else:
            # Leaf node
            label_start = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[label_start:pos].strip()
            # Skip optional branch length
            if pos < len(s) and s[pos] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            return label, pos

    parse(0)
    return adj

def bfs_distance(adj, start, end):
    """BFS distance between start and end in an undirected graph."""
    if start == end:
        return 0
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for neighbour in adj[node]:
            if neighbour == end:
                return dist + 1
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))
    return -1   # not connected (shouldn't happen for valid Newick tree)

def solve(data):
    blocks = data.strip().split('\n\n')
    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue
        newick = lines[0].strip()
        leaf_pair = lines[1].strip().split()
        leaf1, leaf2 = leaf_pair[0], leaf_pair[1]
        adj = parse_newick(newick)
        print(bfs_distance(adj, leaf1, leaf2))

if __name__ == '__main__':
    solve(get_input())
