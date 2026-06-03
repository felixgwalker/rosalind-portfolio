# Base Quality Distribution (BPHR)
# Rosalind problem: https://rosalind.info/problems/bphr/
#
# Problem: Given a FASTQ file, for each position in the reads compute the
# average Phred quality score across all reads.  Output one value per
# position on a single space-separated line.
#
# Phred score = ord(quality_char) - 33

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-armory', 'rosalind_bphr.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def solve(data):
    lines = data.splitlines()
    qual_strings = []
    i = 0
    while i + 3 < len(lines):
        qual = lines[i + 2].strip()
        if qual:
            qual_strings.append([ord(c) - 33 for c in qual])
        i += 4

    if not qual_strings:
        return

    read_len = max(len(q) for q in qual_strings)
    result = []
    for pos in range(read_len):
        scores = [q[pos] for q in qual_strings if pos < len(q)]
        result.append(f"{sum(scores) / len(scores):.1f}")
    print(' '.join(result))

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
