# BA9J — Reconstruct a String from its Burrows-Wheeler Transform
# https://rosalind.info/problems/ba9j/
#
# Given: BWT string. Return: the original string.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9j.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def ibwt(bwt_str):
    n = len(bwt_str)
    # Sort BWT to get first column
    first = sorted(bwt_str)
    # Build last-to-first mapping
    # Count occurrences before each position
    from collections import defaultdict
    count = defaultdict(int)
    last_to_first = []
    char_rank = {}
    for ch in sorted(set(bwt_str)):
        char_rank[ch] = sum(1 for c in first[:first.index(ch)] if c == ch)

    # Build the sorted first column indices
    first_count = defaultdict(int)
    last_rank = []
    for ch in bwt_str:
        last_rank.append(first_count[ch])
        first_count[ch] += 1

    first_occ = {}
    for i, ch in enumerate(first):
        if ch not in first_occ:
            first_occ[ch] = i

    # Follow the chain
    result = []
    row = 0
    for _ in range(n):
        ch = bwt_str[row]
        result.append(ch)
        row = first_occ[ch] + last_rank[row]
    return ''.join(reversed(result))

def solve(data):
    print(ibwt(data.strip()))

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
