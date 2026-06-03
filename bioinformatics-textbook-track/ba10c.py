# BA10C — Implement the Viterbi Algorithm
# https://rosalind.info/problems/ba10c/
#
# Given: a string x, alphabet Σ, states, transition matrix T, and emission matrix E.
# Return: the most probable hidden path.

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba10c.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_hmm(lines):
    """Parse HMM input: x, alphabet, states, transition, emission."""
    x = lines[0].strip()
    alphabet = lines[2].strip().split()
    states = lines[4].strip().split()
    trans = {}; emit = {}
    i = 6
    while i < len(lines) and lines[i].strip() and lines[i].strip() != '--------':
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

def viterbi(x, states, trans, emit):
    n = len(states)
    T = len(x)
    NEG_INF = float('-inf')
    # dp[t][s] = log prob of best path ending in state s at time t
    dp = [{s: NEG_INF for s in states} for _ in range(T)]
    backtrack = [{s: None for s in states} for _ in range(T)]
    for s in states:
        dp[0][s] = math.log(1.0/n) + math.log(emit[s].get(x[0], 1e-10))
    for t in range(1, T):
        for s in states:
            log_e = math.log(emit[s].get(x[t], 1e-10))
            best = NEG_INF; best_prev = None
            for prev in states:
                lp = dp[t-1][prev] + math.log(trans[prev].get(s, 1e-10)) + log_e
                if lp > best: best, best_prev = lp, prev
            dp[t][s] = best; backtrack[t][s] = best_prev
    # Traceback
    last = max(states, key=lambda s: dp[T-1][s])
    path = [last]
    for t in range(T-1, 0, -1):
        path.append(backtrack[t][path[-1]])
    return ''.join(reversed(path))

def solve(data):
    lines = data.splitlines()
    x, alpha, states, trans, emit = parse_hmm(lines)
    print(viterbi(x, states, trans, emit))

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
