# BA9A — Construct a Trie from a Collection of Patterns
# https://rosalind.info/problems/ba9a/
#
# Given: a list of strings. Return: the adjacency list of the trie of these strings.
# Node 1 = root. Each edge labeled with a character.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba9a.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    strings = [l.strip() for l in data.splitlines() if l.strip()]
    nodes = [{}]; nodes.append({})   # nodes[0] unused, nodes[1] = root
    node_count = 1; edges = []
    for s in strings:
        cur = 1
        for ch in s:
            if ch not in nodes[cur]:
                node_count += 1; nodes.append({})
                nodes[cur][ch] = node_count
                edges.append((cur, node_count, ch))
            cur = nodes[cur][ch]
    for a, b, c in edges:
        print(f"{a}->{b}:{c}")

if __name__ == '__main__': solve(get_input())
