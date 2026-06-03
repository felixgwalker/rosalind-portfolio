# Read Quality Distribution (FILT)
# Rosalind problem: https://rosalind.info/problems/filt/
#
# Problem: Given a FASTQ file and an integer T, return the percentage
# of reads with average Phred quality score >= T (rounded to 6 decimal places).
#
# Phred score = ord(quality_char) - 33

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-armory', 'rosalind_filt.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def avg_quality(qual_str):
    return sum(ord(c) - 33 for c in qual_str) / len(qual_str)

def solve(data):
    lines = data.splitlines()
    threshold = int(lines[0].strip())
    total = 0
    passing = 0
    i = 1
    while i + 3 <= len(lines):
        qual = lines[i + 2].strip()
        if qual:
            total += 1
            if avg_quality(qual) >= threshold:
                passing += 1
        i += 4
    pct = (passing / total * 100) if total else 0.0
    print(f"{pct:.6f}")

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
