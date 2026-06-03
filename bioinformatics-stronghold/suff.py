# Encoding Suffix Trees (SUFF)
# Rosalind problem: https://rosalind.info/problems/suff/
#
# Problem: Given a DNA string s (in FASTA), construct its suffix tree and output
# the edge labels (all substrings that label an edge in the suffix tree), one
# per line in any order.
#
# Algorithm: Build a compressed trie of all suffixes using an O(n²) approach
# (inserting each suffix into the trie and compressing chains of single-child nodes).
# A true Ukkonen's O(n) algorithm is omitted for clarity.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_suff.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    parts = []
    for line in text.splitlines():
        if not line.startswith('>'):
            parts.append(line.strip())
    return ''.join(parts)

class SuffixTree:
    """Compact suffix trie — each node stores a dict of first_char -> (edge_label, child)."""

    def __init__(self, s):
        self.root = {}
        for i in range(len(s)):
            self._insert(s[i:])

    def _insert(self, suffix):
        node = self.root
        while suffix:
            first = suffix[0]
            if first not in node:
                # New leaf: store the full remaining suffix as the edge label
                node[first] = [suffix, {}]
                return
            edge_label, child = node[first]
            # Find the length of the common prefix
            k = 0
            while k < len(edge_label) and k < len(suffix) and edge_label[k] == suffix[k]:
                k += 1
            if k == len(edge_label):
                # Edge label is a prefix of suffix — go deeper
                node = child
                suffix = suffix[k:]
            else:
                # Split the edge at position k
                shared = edge_label[:k]
                rest_edge = edge_label[k:]
                rest_suffix = suffix[k:]
                # Create a new internal node
                new_child = {rest_edge[0]: [rest_edge, child]}
                node[first] = [shared, new_child]
                # Insert the remaining suffix into the new internal node
                if rest_suffix:
                    new_child[rest_suffix[0]] = [rest_suffix, {}]
                return

def collect_edges(node, result):
    for first_char, (edge_label, child) in node.items():
        result.append(edge_label)
        collect_edges(child, result)

def solve(data):
    s = parse_fasta(data)
    # Append sentinel '$' to ensure all leaves are unique
    s = s + '$'
    st = SuffixTree(s)
    edges = []
    collect_edges(st.root, edges)
    for e in edges:
        print(e)

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
