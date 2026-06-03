# BA10A — Compute the Probability of a Hidden Path
# https://rosalind.info/problems/ba10a/
#
# Given: a hidden path π, transition matrix, and emission matrix.
# Return: the probability of the hidden path (product of transition probabilities).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba10a.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    path = lines[0].strip()
    states = lines[2].strip().split()
    # Parse transition matrix
    trans = {}
    for line in lines[4:]:
        if not line.strip(): break
        parts = line.split()
        frm = parts[0]
        trans[frm] = {states[i]: float(parts[i+1]) for i in range(len(states))}
    n = len(states)
    prob = 1.0 / n   # equal initial probability for each state
    for i in range(1, len(path)):
        prob *= trans[path[i-1]][path[i]]
    print(f"{prob:.2e}")

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
