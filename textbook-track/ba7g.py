# BA7G — Adapt SmallParsimony to Unrooted Trees
# https://rosalind.info/problems/ba7g/
#
# Given: an unrooted binary tree with labeled leaves. Return: parsimony score.
# Root the tree at an arbitrary internal edge, then apply SmallParsimony.

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba7g.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    adj = defaultdict(list); labels = {}
    for line in lines[1:]:
        line = line.strip()
        if not line: continue
        parts = line.split('->')
        u, v = parts[0].strip(), parts[1].strip()
        adj[u].append(v); adj[v].append(u)
        if not v[0].isdigit(): labels[v] = v

    seq_len = len(next(iter(labels.values()))) if labels else 0
    nodes = set(adj.keys()) | {v for nb in adj.values() for v in nb}
    leaves = {v for v in nodes if len(adj[v]) == 1 and not v[0].isdigit()}

    # Find root: add virtual edge to split an internal edge
    internal = [v for v in nodes if v not in leaves]
    if not internal: print(0); return
    root = internal[0]

    def parsimony_score(node, parent, memo):
        if node in leaves:
            return [{labels[node][i]} for i in range(seq_len)], 0
        children = [c for c in adj[node] if c != parent]
        score = 0
        sets = []
        child_sets = []
        for ch in children:
            csets, cscore = parsimony_score(ch, node, memo)
            score += cscore; child_sets.append(csets)
        for i in range(seq_len):
            intersection = child_sets[0][i]
            for cs in child_sets[1:]: intersection &= cs[i]
            if intersection:
                sets.append(intersection)
            else:
                union = set()
                for cs in child_sets: union |= cs[i]
                sets.append(union); score += 1
        return sets, score

    _, score = parsimony_score(root, None, {})
    print(score)

if __name__ == '__main__': solve(get_input())
