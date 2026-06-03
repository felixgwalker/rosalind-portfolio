# BA6J — Implement 2-BreakOnGenomeGraph
# https://rosalind.info/problems/ba6j/
#
# Given: a genome graph (set of colored edges) and four nodes (i1, i2, i3, i4).
# Return: the genome graph resulting from applying the 2-break (i1,i2),(i3,i4)
# → (i1,i3),(i2,i4).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6j.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    # Parse edge set
    edges = set()
    for part in lines[0].strip().split('), ('):
        part = part.strip().strip('()')
        u, v = map(int, part.split(','))
        edges.add((min(u,v), max(u,v)))
    i1, i2, i3, i4 = map(int, lines[1].strip().split(','))
    # Remove edges (i1,i2) and (i3,i4), add (i1,i3) and (i2,i4)
    edges.discard((min(i1,i2), max(i1,i2)))
    edges.discard((min(i3,i4), max(i3,i4)))
    edges.add((min(i1,i3), max(i1,i3)))
    edges.add((min(i2,i4), max(i2,i4)))
    result = ', '.join(f'({u}, {v})' for u, v in sorted(edges))
    print(result)

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
