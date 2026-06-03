# BA10I — Implement Viterbi Learning
# https://rosalind.info/problems/ba10i/
#
# Given: number of iterations, emitted string x, alphabet, states,
#        initial transition T and emission E matrices.
# Return: updated T and E after Viterbi learning (hard EM).
#
# Viterbi learning alternates between:
#   1. Find the Viterbi path for x given current T, E.
#   2. Re-estimate T, E by counting transitions/emissions in that path.

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba10i.txt')
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

def viterbi(x, states, trans, emit):
    n = len(states); T = len(x)
    NEG_INF = float('-inf')
    dp = [{s: NEG_INF for s in states} for _ in range(T)]
    bt = [{s: None for s in states} for _ in range(T)]
    for s in states:
        dp[0][s] = math.log(1.0/n + 1e-300) + math.log(emit[s].get(x[0],1e-300))
    for t in range(1, T):
        for s in states:
            log_e = math.log(emit[s].get(x[t],1e-300))
            best = NEG_INF; bprev = None
            for prev in states:
                lp = dp[t-1][prev] + math.log(trans[prev].get(s,1e-300)) + log_e
                if lp > best: best, bprev = lp, prev
            dp[t][s] = best; bt[t][s] = bprev
    last = max(states, key=lambda s: dp[T-1][s])
    path = [last]
    for t in range(T-1, 0, -1): path.append(bt[t][path[-1]])
    return ''.join(reversed(path))

def reestimate(x, path, alphabet, states):
    from collections import defaultdict
    tc = defaultdict(lambda: defaultdict(float))
    ec = defaultdict(lambda: defaultdict(float))
    for i in range(len(path)-1): tc[path[i]][path[i+1]] += 1
    for xi, si in zip(x, path): ec[si][xi] += 1
    trans = {}
    for s in states:
        total = sum(tc[s].values()) or 1
        trans[s] = {t: tc[s][t]/total for t in states}
    emit = {}
    for s in states:
        total = sum(ec[s].values()) or 1
        emit[s] = {a: ec[s][a]/total for a in alphabet}
    return trans, emit

def solve(data):
    lines = data.splitlines()
    iters = int(lines[0].strip())
    x, alphabet, states, trans, emit = parse_hmm(lines[2:])
    for _ in range(iters):
        path = viterbi(x, states, trans, emit)
        trans, emit = reestimate(x, path, alphabet, states)
    # Output transition matrix
    print('\t'.join([''] + states))
    for s in states:
        print('\t'.join([s] + [f"{trans[s].get(t,0):.3f}" for t in states]))
    print('--------')
    print('\t'.join([''] + alphabet))
    for s in states:
        print('\t'.join([s] + [f"{emit[s].get(a,0):.3f}" for a in alphabet]))

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
