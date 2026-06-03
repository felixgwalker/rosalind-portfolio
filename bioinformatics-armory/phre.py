# Phred Quality Scores (PHRE)
# Rosalind problem: https://rosalind.info/problems/phre/
#
# Problem: Given a FASTQ file and an integer T, return the number of reads
# whose average Phred quality score is >= T.
#
# Phred score = ord(quality_char) - 33  (Phred+33 / Sanger encoding)

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-armory', 'rosalind_phre.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def avg_quality(qual_str):
    return sum(ord(c) - 33 for c in qual_str) / len(qual_str)

def solve(data):
    lines = data.splitlines()
    threshold = int(lines[0].strip())
    count = 0
    i = 1
    while i + 3 <= len(lines):
        qual = lines[i + 2].strip()   # 4-line FASTQ: header, seq, +, qual
        if qual and avg_quality(qual) >= threshold:
            count += 1
        i += 4
    print(count)

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
