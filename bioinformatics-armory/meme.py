# New Motif Discovery (MEME)
# Rosalind problem: https://rosalind.info/problems/meme/
#
# Problem: Given a collection of DNA strings in FASTA format and a motif
# width k (first non-FASTA line of input), find the most conserved k-mer
# using expectation-maximization (EM) motif search.
#
# Returns the consensus string of the discovered motif.

import os
import sys
import math

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-armory', 'rosalind_meme.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    records, cur_id, parts = [], None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if cur_id is not None:
                records.append(''.join(parts))
            cur_id, parts = line[1:], []
        else:
            parts.append(line)
    if cur_id is not None:
        records.append(''.join(parts))
    return records

BASES = 'ACGT'
BG = 0.25  # uniform background frequency

def build_pwm(seqs, positions, k):
    """Position frequency matrix with pseudocount 1."""
    counts = [[1.0] * 4 for _ in range(k)]
    for seq, pos in zip(seqs, positions):
        for j, base in enumerate(seq[pos:pos + k]):
            idx = BASES.find(base)
            if idx >= 0:
                counts[j][idx] += 1.0
    pwm = []
    for col in counts:
        total = sum(col)
        pwm.append([v / total for v in col])
    return pwm

def log_odds(seq, pos, k, pwm):
    score = 0.0
    for j, base in enumerate(seq[pos:pos + k]):
        idx = BASES.find(base)
        if idx >= 0:
            score += math.log(pwm[j][idx] / BG)
    return score

def best_pos(seq, k, pwm):
    return max(range(len(seq) - k + 1), key=lambda p: log_odds(seq, p, k, pwm))

def consensus(pwm):
    return ''.join(BASES[max(range(4), key=lambda b: pwm[j][b])] for j in range(len(pwm)))

def em_run(seqs, k, seed_idx):
    """One EM run seeded with the k-mer at position seed_idx in seqs[0]."""
    positions = [seed_idx] + [0] * (len(seqs) - 1)
    for _ in range(100):
        pwm = build_pwm(seqs, positions, k)
        new_pos = [best_pos(s, k, pwm) for s in seqs]
        if new_pos == positions:
            break
        positions = new_pos
    pwm = build_pwm(seqs, positions, k)
    score = sum(log_odds(s, p, k, pwm) for s, p in zip(seqs, positions))
    return score, consensus(pwm)

def solve(data):
    lines = data.splitlines()
    k = None
    fasta_start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not stripped.startswith('>') and stripped.isdigit():
            k = int(stripped)
            fasta_start = i + 1
            break
        if stripped.startswith('>'):
            fasta_start = i
            break

    seqs = [s.upper() for s in parse_fasta('\n'.join(lines[fasta_start:])) if s]
    if not seqs:
        return
    if k is None:
        k = min(8, min(len(s) for s in seqs))

    best_score, best_consensus = float('-inf'), ''
    for seed in range(len(seqs[0]) - k + 1):
        score, cons = em_run(seqs, k, seed)
        if score > best_score:
            best_score, best_consensus = score, cons
    print(best_consensus)

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
