# BA7A — Compute Distances Between Leaves
# https://rosalind.info/problems/ba7a/
#
# Given: an integer n and an n×n additive distance matrix.
# Return: a weighted tree whose leaf-to-leaf distances match the matrix.
# Output: the tree as an adjacency list with edge weights, then the matrix.
# (This problem asks to reconstruct and output the additive tree.)

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba7a.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    # This problem asks: "Given a tree with weighted edges, output the n×n matrix
    # of distances between all leaf pairs." We assume the input is the tree adjacency list.
    lines = data.splitlines()
    n = int(lines[0].strip())
    from collections import defaultdict
    adj = defaultdict(list)
    for line in lines[1:]:
        line = line.strip()
        if not line: continue
        # Format: "u->v:weight"
        parts = line.split('->')
        u = int(parts[0].strip())
        v_w = parts[1].split(':')
        v, w = int(v_w[0].strip()), float(v_w[1].strip())
        adj[u].append((v, w)); adj[v].append((u, w))
    # BFS to compute all leaf-leaf distances
    from collections import deque
    leaves = [i for i in range(n)]
    result = [[0]*n for _ in range(n)]
    for src in leaves:
        dist = {src: 0}
        queue = deque([src])
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + w
                    queue.append(v)
        for tgt in leaves:
            result[src][tgt] = dist.get(tgt, 0)
    for row in result:
        print('\t'.join(str(int(x)) if x==int(x) else f'{x:.0f}' for x in row))

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
