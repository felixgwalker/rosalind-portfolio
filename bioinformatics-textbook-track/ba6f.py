# BA6F — Implement ChromosomeToCycle
# https://rosalind.info/problems/ba6f/
#
# Given: a signed permutation (chromosome).
# Return: the corresponding cycle of nodes.
# For each element x: if x>0: nodes 2x-1, 2x; if x<0: nodes -2x, -2x-1.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6f.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    perm = list(map(int, data.strip().strip('()').split()))
    nodes = []
    for x in perm:
        if x > 0: nodes.extend([2*x-1, 2*x])
        else: nodes.extend([-2*x, -2*x-1])
    print('(' + ' '.join(map(str, nodes)) + ')')

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
