# BA10J — Implement Baum-Welch Learning
# https://rosalind.info/problems/ba10j/
#
# Given: number of iterations, emitted string x, alphabet, states, T, E.
# Return: updated T and E after Baum-Welch (soft EM).
#
# Baum-Welch alternates:
#   1. E-step: compute forward/backward probabilities.
#   2. M-step: re-estimate T, E from expected counts.

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba10j.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

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

def forward_log(x, states, trans, emit):
    n = len(states); T = len(x)
    NEG_INF = float('-inf')
    fwd = [{s: NEG_INF for s in states} for _ in range(T)]
    for s in states:
        fwd[0][s] = math.log(1.0/n + 1e-300) + math.log(emit[s].get(x[0],1e-300))
    for t in range(1, T):
        for s in states:
            log_e = math.log(emit[s].get(x[t],1e-300))
            vals = [fwd[t-1][prev] + math.log(trans[prev].get(s,1e-300)) for prev in states]
            mv = max(vals)
            fwd[t][s] = mv + math.log(sum(math.exp(v-mv) for v in vals)) + log_e
    return fwd

def backward_log(x, states, trans, emit):
    T = len(x)
    NEG_INF = float('-inf')
    bwd = [{s: 0.0 for s in states} for _ in range(T)]
    for t in range(T-2, -1, -1):
        for s in states:
            vals = [math.log(trans[s].get(nxt,1e-300)) + math.log(emit[nxt].get(x[t+1],1e-300)) + bwd[t+1][nxt]
                    for nxt in states]
            mv = max(vals)
            bwd[t][s] = mv + math.log(sum(math.exp(v-mv) for v in vals))
    return bwd

def baum_welch_step(x, states, alphabet, trans, emit):
    T = len(x)
    fwd = forward_log(x, states, trans, emit)
    bwd = backward_log(x, states, trans, emit)
    # Compute gamma (state occupancy)
    gamma = []
    for t in range(T):
        vals = {s: fwd[t][s] + bwd[t][s] for s in states}
        mv = max(vals.values())
        log_total = mv + math.log(sum(math.exp(v-mv) for v in vals.values()))
        gamma.append({s: math.exp(vals[s] - log_total) for s in states})
    # Compute xi (transition occupancy)
    from collections import defaultdict
    trans_count = defaultdict(lambda: defaultdict(float))
    emit_count = defaultdict(lambda: defaultdict(float))
    for t in range(T-1):
        total = 0
        xi = {}
        for s in states:
            for nxt in states:
                v = math.exp(fwd[t][s] + math.log(trans[s].get(nxt,1e-300)) +
                             math.log(emit[nxt].get(x[t+1],1e-300)) + bwd[t+1][nxt])
                xi[(s,nxt)] = v
                total += v
        if total > 0:
            for (s,nxt), v in xi.items():
                trans_count[s][nxt] += v/total
    for t in range(T):
        for s in states:
            emit_count[s][x[t]] += gamma[t][s]
    new_trans = {}
    for s in states:
        total = sum(trans_count[s].values()) or 1
        new_trans[s] = {t: trans_count[s][t]/total for t in states}
    new_emit = {}
    for s in states:
        total = sum(emit_count[s].values()) or 1
        new_emit[s] = {a: emit_count[s][a]/total for a in alphabet}
    return new_trans, new_emit

def solve(data):
    lines = data.splitlines()
    iters = int(lines[0].strip())
    x, alphabet, states, trans, emit = parse_hmm(lines[2:])
    for _ in range(iters):
        trans, emit = baum_welch_step(x, states, alphabet, trans, emit)
    print('\t'.join([''] + states))
    for s in states:
        print('\t'.join([s] + [f"{trans[s].get(t,0):.3f}" for t in states]))
    print('--------')
    print('\t'.join([''] + alphabet))
    for s in states:
        print('\t'.join([s] + [f"{emit[s].get(a,0):.3f}" for a in alphabet]))

if __name__ == '__main__': solve(get_input())
