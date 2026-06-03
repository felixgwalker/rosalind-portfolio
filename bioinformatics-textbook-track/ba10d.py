# BA10D — Compute the Probability of a String Emitted by an HMM
# https://rosalind.info/problems/ba10d/
#
# Given: emitted string x, alphabet, states, transition T, emission E.
# Return: P(x) = sum over all paths of P(x|π) (forward algorithm).

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba10d.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_hmm(lines):
    x = lines[0].strip()
    alphabet = lines[2].strip().split()
    states = lines[4].strip().split()
    trans = {}; emit = {}; i = 6
    while i < len(lines) and lines[i].strip() and '---' not in lines[i]:
        parts = lines[i].split()
        if parts[0] in states:
            trans[parts[0]] = {states[j]: float(parts[j+1]) for j in range(len(states))}
        i += 1
    i += 1
    while i < len(lines) and lines[i].strip():
        parts = lines[i].split()
        if parts[0] in states:
            emit[parts[0]] = {alphabet[j]: float(parts[j+1]) for j in range(len(alphabet))}
        i += 1
    return x, alphabet, states, trans, emit

def forward(x, states, trans, emit):
    n = len(states)
    T = len(x)
    dp = {s: math.log(1.0/n) + math.log(emit[s].get(x[0],1e-300)) for s in states}
    for t in range(1, T):
        new_dp = {}
        for s in states:
            log_e = math.log(emit[s].get(x[t],1e-300))
            vals = [dp[prev] + math.log(trans[prev].get(s,1e-300)) for prev in states]
            max_val = max(vals)
            log_sum = max_val + math.log(sum(math.exp(v-max_val) for v in vals))
            new_dp[s] = log_sum + log_e
        dp = new_dp
    vals = list(dp.values())
    max_val = max(vals)
    return max_val + math.log(sum(math.exp(v-max_val) for v in vals))

def solve(data):
    lines = data.splitlines()
    x, alpha, states, trans, emit = parse_hmm(lines)
    print(f"{math.exp(forward(x, states, trans, emit)):.2e}")

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
