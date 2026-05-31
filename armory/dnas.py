# Identifying DNA Strings (DNAS)
# Rosalind problem: https://rosalind.info/problems/dnas/
#
# Problem: Access the NCBI Nucleotide database for Homo sapiens records and
# find the protein encoded by a specific mRNA accession.
# Given: an mRNA accession number.
# Return: the coding sequence (CDS) feature translated to protein.
#
# Requires internet access to NCBI Entrez API.

import os
import sys
import urllib.request
import urllib.parse

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_dnas.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

ENTREZ_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_genbank(accession):
    """Fetch GenBank record in FASTA format."""
    params = urllib.parse.urlencode({
        'db': 'nucleotide',
        'id': accession,
        'rettype': 'fasta',
        'retmode': 'text'
    })
    url = f"{ENTREZ_BASE}efetch.fcgi?{params}"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode('utf-8')

def solve(data):
    accession = data.strip()
    try:
        fasta = fetch_genbank(accession)
        print(fasta.strip())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    solve(get_input())
