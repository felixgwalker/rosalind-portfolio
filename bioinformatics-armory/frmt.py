# Data Formats (FRMT)
# Rosalind problem: https://rosalind.info/problems/frmt/
#
# Problem: Given at most 10 UniProt accession IDs, download each protein
# sequence from UniProt and return the FASTA-format sequence of the one with
# the shortest length (ties broken lexicographically by ID).
#
# Requires internet access to UniProt API.

import os
import sys
import urllib.request

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-armory', 'rosalind_frmt.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def fetch_fasta(uniprot_id):
    """Fetch FASTA sequence from UniProt REST API."""
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode('utf-8').strip()

def parse_fasta_single(fasta_text):
    """Return (header, sequence) from a single FASTA record."""
    lines = fasta_text.strip().splitlines()
    header = lines[0]
    seq = ''.join(lines[1:])
    return header, seq

def solve(data):
    ids = data.split()
    best_id = None
    best_len = float('inf')
    best_fasta = None

    for uid in ids:
        try:
            fasta = fetch_fasta(uid)
            header, seq = parse_fasta_single(fasta)
            if len(seq) < best_len or (len(seq) == best_len and uid < best_id):
                best_len = len(seq)
                best_id = uid
                best_fasta = fasta
        except Exception:
            pass

    if best_fasta:
        print(best_fasta)

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
