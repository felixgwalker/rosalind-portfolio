# BA7F — Implement SmallParsimony
# https://rosalind.info/problems/ba7f/
#
# Given: a rooted binary tree with labeled leaves (DNA strings).
# Return: the parsimony score and the ancestral labels.
# Uses the Fitch algorithm (bottom-up then top-down).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba7f.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n = int(lines[0].strip())
    adj = defaultdict(list); labels = {}
    for line in lines[1:]:
        line = line.strip()
        if not line: continue
        parts = line.split('->')
        u, v = parts[0].strip(), parts[1].strip()
        adj[u].append(v)
        if not v[0].isdigit(): labels[v] = v   # leaf label = sequence

    # Build node sets
    all_nodes = set(adj.keys()) | {v for nb in adj.values() for v in nb}
    leaves = {v for v in all_nodes if not adj[v]}

    if not labels:
        print("Input needs leaf labels")
        return

    # Find root (in-degree 0)
    children = set(v for nb in adj.values() for v in nb)
    root = next(n for n in adj if n not in children)

    seq_len = len(next(iter(labels.values())))
    # Fitch algorithm
    node_sets = {}   # character sets per node per position

    def fitch_up(node):
        if node in leaves:
            node_sets[node] = [{labels[node][i]} for i in range(seq_len)]
            return 0
        ch = adj[node]
        score = sum(fitch_up(c) for c in ch)
        sets = []
        for i in range(seq_len):
            intersection = node_sets[ch[0]][i] & node_sets[ch[1]][i] if len(ch)>1 else node_sets[ch[0]][i]
            if intersection:
                sets.append(intersection)
            else:
                sets.append(node_sets[ch[0]][i] | (node_sets[ch[1]][i] if len(ch)>1 else set()))
                score += 1
        node_sets[node] = sets
        return score

    score = fitch_up(root)
    print(score)

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
