# BA5D — Find the Longest Path in a DAG
# https://rosalind.info/problems/ba5d/
#
# Given: a DAG (source, sink, and weighted edges).
# Return: the length of the longest path and the path itself.

import os, sys
from collections import defaultdict, deque

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba5d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    source = int(lines[0].strip())
    sink = int(lines[1].strip())
    adj = defaultdict(list)
    in_deg = defaultdict(int)
    nodes = set()
    for line in lines[2:]:
        if not line.strip():
            continue
        parts = line.split('->')
        u = int(parts[0].strip())
        v_w = parts[1].split(':')
        v, w = int(v_w[0].strip()), int(v_w[1].strip())
        adj[u].append((v, w))
        in_deg[v] += 1
        nodes.update([u, v])

    # Topological sort
    queue = deque(n for n in nodes if in_deg[n] == 0)
    topo = []
    temp_in = dict(in_deg)
    for n in nodes:
        temp_in.setdefault(n, 0)
    while queue:
        u = queue.popleft()
        topo.append(u)
        for v, _ in adj[u]:
            temp_in[v] -= 1
            if temp_in[v] == 0:
                queue.append(v)

    dist = {n: float('-inf') for n in nodes}
    dist[source] = 0
    pred = {n: -1 for n in nodes}
    for u in topo:
        if dist[u] == float('-inf'):
            continue
        for v, w in adj[u]:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

    # Reconstruct path
    path = []
    v = sink
    while v != -1:
        path.append(v)
        v = pred[v]
    path.reverse()

    print(dist[sink])
    print('->'.join(map(str, path)))

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
