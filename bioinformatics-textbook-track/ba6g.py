# BA6G — Implement CycleToChromosome
# https://rosalind.info/problems/ba6g/
#
# Given: a sequence of nodes forming a cycle.
# Return: the corresponding chromosome (signed permutation).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba6g.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    nodes = list(map(int, data.strip().strip('()').split()))
    chromosome = []
    for i in range(0, len(nodes), 2):
        t, h = nodes[i], nodes[i+1]
        if h == t + 1:   # positive element: t = 2x-1, h = 2x → x = h/2
            chromosome.append(h // 2)
        else:            # negative element: h = 2x-1, t = 2x → x = t/2 (negative)
            chromosome.append(-(t // 2))
    print('(' + ' '.join(map(str, chromosome)) + ')')

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
