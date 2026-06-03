# Transforming FASTQ to FASTA (TFSQ)
# Rosalind problem: https://rosalind.info/problems/tfsq/
#
# Problem: Given a FASTQ file, convert it to FASTA format by stripping
# the quality score lines and renaming headers from @ to >.
#
# FASTQ format (4 lines per read): @id / sequence / + / quality
# FASTA format (2 lines per record): >id / sequence

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-armory', 'rosalind_tfsq.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def solve(data):
    lines = data.splitlines()
    out = []
    i = 0
    while i + 3 < len(lines):
        header = lines[i].strip()
        seq    = lines[i + 1].strip()
        i += 4
        if not header:
            continue
        out.append('>' + header[1:])
        out.append(seq)
    print('\n'.join(out))

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
