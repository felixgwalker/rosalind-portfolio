# Finding a Spliced Motif (SSEQ)
# Rosalind problem: https://rosalind.info/problems/sseq/
#
# Problem: Given two DNA strings s and t (in FASTA format), find a subsequence
# of s whose characters match t in order. Return the 1-indexed positions in s
# of the characters forming this subsequence.
#
# (t is a subsequence of s means we can delete characters from s, without
# reordering, to obtain t. This models the spliced alignment of an exon t
# within a genome s.)
#
# Algorithm: Greedy single scan — walk s left-to-right; whenever s[i] matches
# the next unmatched character of t, record i+1. O(|s| + |t|).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_sseq.txt')
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
                records.append(''.join(parts))
            current_id, parts = line[1:], []
        else:
            parts.append(line)
    if current_id is not None:
        records.append(''.join(parts))
    return records

def solve(data):
    records = parse_fasta(data)
    s, t = records[0], records[1]
    positions = []
    j = 0   # pointer into t
    for i, ch in enumerate(s):
        if j < len(t) and ch == t[j]:
            positions.append(i + 1)    # 1-indexed
            j += 1
    print(' '.join(map(str, positions)))

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
