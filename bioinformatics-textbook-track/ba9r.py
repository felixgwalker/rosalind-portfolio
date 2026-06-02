# BA9R — Construct a Suffix Tree from a Suffix Array
# https://rosalind.info/problems/ba9r/
#
# Given: A string Text.
# Return: The edges of the suffix tree of Text, where each edge is labeled
#         by the substring of Text it represents.
#
# We build the suffix array, compute the LCP array via Kasai's algorithm,
# then reconstruct the suffix tree's edge-label strings.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9r.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def build_suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

def build_lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i, suf in enumerate(sa):
        rank[suf] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0: h -= 1
    return lcp

def suffix_tree_edges(text):
    if not text.endswith('$'):
        text += '$'
    n = len(text)
    sa = build_suffix_array(text)
    lcp = build_lcp_array(text, sa)

    # Use a stack-based approach to reconstruct edges from SA+LCP
    # Each edge corresponds to the portion of a suffix not shared with
    # the previous suffix in the sorted order (LCP gives the shared prefix length).
    edges = []
    stack = [(0, 0)]  # (lcp_depth, sa_index) — root has depth 0

    for i in range(n):
        cur_lcp = lcp[i] if i > 0 else 0
        # Pop stack until we find a node whose depth <= cur_lcp
        while len(stack) > 1 and stack[-1][0] > cur_lcp:
            node_depth, node_start = stack.pop()
            parent_depth = max(stack[-1][0], cur_lcp)
            # Edge from parent (depth parent_depth) to child (depth node_depth)
            start = sa[node_start] + parent_depth
            length = node_depth - parent_depth
            edges.append(text[start: start + length])

        if not stack or stack[-1][0] < cur_lcp:
            stack.append((cur_lcp, i))
        elif stack[-1][0] == cur_lcp:
            pass  # merge

        # Leaf edge for suffix sa[i]: from depth cur_lcp to end of suffix
        stack.append((n - sa[i], i))

    # Drain the stack
    while len(stack) > 1:
        node_depth, node_start = stack.pop()
        parent_depth = stack[-1][0]
        start = sa[node_start] + parent_depth
        length = node_depth - parent_depth
        if length > 0:
            edges.append(text[start: start + length])

    return edges

def solve(data):
    text = data.strip()
    for edge in suffix_tree_edges(text):
        print(edge)

if __name__ == '__main__': solve(get_input())
