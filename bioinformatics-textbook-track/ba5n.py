# BA5N — Find a Topological Ordering of a DAG
# https://rosalind.info/problems/ba5n/
#
# Given: a DAG (adjacency list). Return: a topological ordering.

import os, sys
from collections import defaultdict, deque

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba5n.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    adj = defaultdict(list)
    in_deg = defaultdict(int)
    nodes = set()
    for line in data.splitlines():
        line = line.strip()
        if not line: continue
        parts = line.split('->')
        u = int(parts[0].strip())
        for v in parts[1].split(','):
            v = int(v.strip())
            adj[u].append(v)
            in_deg[v] += 1
            nodes.update([u, v])
    queue = deque(n for n in nodes if in_deg[n] == 0)
    topo = []
    temp_in = dict(in_deg)
    while queue:
        u = queue.popleft(); topo.append(u)
        for v in adj[u]:
            temp_in[v] -= 1
            if temp_in[v] == 0: queue.append(v)
    print(', '.join(map(str, topo)))

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
