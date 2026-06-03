# BA9A — Construct a Trie from a Collection of Patterns
# https://rosalind.info/problems/ba9a/
#
# Given: a list of strings. Return: the adjacency list of the trie of these strings.
# Node 1 = root. Each edge labeled with a character.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9a.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

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
