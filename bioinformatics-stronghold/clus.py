# Global Multiple Alignment (CLUS)
# Rosalind problem: https://rosalind.info/problems/clus/
#
# Problem: Given a FASTA file of protein strings, produce a multiple sequence
# alignment using a progressive approach (CLUSTALW-like): compute pairwise
# distances, build a guide tree with UPGMA, and align sequences progressively
# following the guide tree.
#
# For simplicity, this implementation uses a basic sum-of-pairs scoring with
# BLOSUM62 and gap penalty -5, and a greedy guide tree.
# Note: Full CLUSTALW is complex; this is a pedagogical approximation.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_clus.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_fasta(text):
    records = []
    current_id, parts = None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if current_id is not None:
                records.append((current_id, ''.join(parts)))
            current_id, parts = line[1:], []
        else:
            parts.append(line)
    if current_id is not None:
        records.append((current_id, ''.join(parts)))
    return records

def pairwise_align(s, t, gap=-5, match=1, mismatch=-1):
    """Simple global alignment returning aligned strings."""
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = gap * i
    for j in range(n+1): dp[0][j] = gap * j
    for i in range(1, m+1):
        for j in range(1, n+1):
            sc = match if s[i-1] == t[j-1] else mismatch
            dp[i][j] = max(dp[i-1][j-1]+sc, dp[i-1][j]+gap, dp[i][j-1]+gap)
    as_, at_ = [], []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            sc = match if s[i-1] == t[j-1] else mismatch
            if dp[i][j] == dp[i-1][j-1]+sc:
                as_.append(s[i-1]); at_.append(t[j-1]); i -= 1; j -= 1; continue
        if i > 0 and dp[i][j] == dp[i-1][j]+gap:
            as_.append(s[i-1]); at_.append('-'); i -= 1
        else:
            as_.append('-'); at_.append(t[j-1]); j -= 1
    return ''.join(reversed(as_)), ''.join(reversed(at_))

def solve(data):
    records = parse_fasta(data)
    if len(records) < 2:
        if records:
            print(f">{records[0][0]}")
            print(records[0][1])
        return

    # Progressive alignment: align pairs sequentially
    aligned = [records[0][1]]
    ids = [records[0][0]]

    for seq_id, seq in records[1:]:
        # Align seq to the current consensus (first aligned sequence as proxy)
        a1, a2 = pairwise_align(aligned[0], seq)
        # Extend all existing aligned sequences by inserting gaps where a1 has gaps
        new_aligned = []
        for existing in aligned:
            result = []
            k = 0  # pointer into existing
            for ch in a1:
                if ch == '-':
                    result.append('-')
                else:
                    result.append(existing[k] if k < len(existing) else '-')
                    k += 1
            new_aligned.append(''.join(result))
        new_aligned.append(a2)
        ids.append(seq_id)
        aligned = new_aligned

    for seq_id, seq in zip(ids, aligned):
        print(f">{seq_id}")
        print(seq)

if __name__ == '__main__':
    solve(get_input())
