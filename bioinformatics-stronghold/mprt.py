# Finding a Protein Motif (MPRT)
# Rosalind problem: https://rosalind.info/problems/mprt/
#
# Problem: Given at most 15 UniProt IDs, fetch each protein's FASTA sequence
# from UniProt, then find all occurrences of the N-glycosylation motif:
#   N{P}[ST]{P}
# which means: N, then any amino acid except P, then S or T, then any except P.
# Output the ID of each sequence that has the motif, followed by the 1-indexed
# positions of each occurrence (overlapping allowed).
#
# Algorithm: Regex-like sliding window to handle overlaps; urllib for fetching.
# Note: requires internet access to UniProt.

import os
import sys
import urllib.request
import re

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_mprt.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def fetch_sequence(uniprot_id):
    """Download FASTA from UniProt and return the amino acid sequence."""
    base_id = uniprot_id.split('-')[0]    # strip isoform suffix e.g. P07814-1
    url = f"https://www.uniprot.org/uniprot/{base_id}.fasta"
    with urllib.request.urlopen(url) as resp:
        fasta = resp.read().decode('utf-8')
    lines = fasta.strip().splitlines()
    return ''.join(l for l in lines if not l.startswith('>'))

def find_nglyc_motif(seq):
    """Return 1-indexed positions of the N-glycosylation motif N{P}[ST]{P}."""
    positions = []
    for i in range(len(seq) - 3):
        # N, then non-P, then S or T, then non-P
        if (seq[i] == 'N' and
                seq[i+1] != 'P' and
                seq[i+2] in 'ST' and
                seq[i+3] != 'P'):
            positions.append(i + 1)   # 1-indexed
    return positions

def solve(data):
    ids = data.splitlines()
    for uid in ids:
        uid = uid.strip()
        if not uid:
            continue
        try:
            seq = fetch_sequence(uid)
            positions = find_nglyc_motif(seq)
            if positions:
                print(uid)
                print(' '.join(map(str, positions)))
        except Exception:
            pass   # skip IDs that can't be fetched

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
