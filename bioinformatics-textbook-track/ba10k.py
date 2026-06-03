# BA10K — Implement the Forward-Backward Algorithm
# https://rosalind.info/problems/ba10k/
#
# Given: A string x, alphabet Σ, state space Σ', transition matrix T,
#        and emission matrix E of an HMM.
# Return: The probability that the HMM was in each state at each step,
#         i.e., the matrix P(πt = k | x) for all t and k.
#
# Uses log-space arithmetic for numerical stability.

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba10k.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_hmm(lines):
    x = lines[0].strip()
    alphabet = lines[2].strip().split()
    states   = lines[4].strip().split()
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

def log(v):
    return math.log(v) if v > 0 else float('-inf')

def log_sum_exp(vals):
    mv = max(vals)
    if mv == float('-inf'): return float('-inf')
    return mv + math.log(sum(math.exp(v - mv) for v in vals))

def forward(x, states, trans, emit):
    T = len(x)
    n = len(states)
    fwd = [{s: float('-inf') for s in states} for _ in range(T)]
    for s in states:
        fwd[0][s] = log(1.0 / n) + log(emit[s].get(x[0], 0))
    for t in range(1, T):
        for s in states:
            log_e = log(emit[s].get(x[t], 0))
            vals = [fwd[t-1][prev] + log(trans[prev].get(s, 0)) for prev in states]
            fwd[t][s] = log_sum_exp(vals) + log_e
    return fwd

def backward(x, states, trans, emit):
    T = len(x)
    bwd = [{s: 0.0 for s in states} for _ in range(T)]
    for t in range(T - 2, -1, -1):
        for s in states:
            vals = [log(trans[s].get(nxt, 0)) + log(emit[nxt].get(x[t+1], 0)) + bwd[t+1][nxt]
                    for nxt in states]
            bwd[t][s] = log_sum_exp(vals)
    return bwd

def solve(data):
    lines = data.splitlines()
    x, alphabet, states, trans, emit = parse_hmm(lines)
    fwd = forward(x, states, trans, emit)
    bwd = backward(x, states, trans, emit)

    T = len(x)
    # Print header
    print('\t' + '\t'.join(states))
    for t in range(T):
        log_probs = {s: fwd[t][s] + bwd[t][s] for s in states}
        log_total = log_sum_exp(list(log_probs.values()))
        probs = [math.exp(log_probs[s] - log_total) if log_total != float('-inf') else 0.0
                 for s in states]
        row = x[t] + '\t' + '\t'.join(f"{p:.4f}" for p in probs)
        print(row)

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
