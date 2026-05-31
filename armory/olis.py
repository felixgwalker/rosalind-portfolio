# Online Bioinformatics Resources (OLIS)
# Rosalind problem: https://rosalind.info/problems/olis/
#
# Problem: This problem tests knowledge of major bioinformatics databases.
# Given: a description of a query (e.g., "find protein from GenBank accession X")
# Return: the relevant information extracted from the appropriate database.
#
# This is largely an exploratory/tutorial problem. The implementation below
# demonstrates how to programmatically access common bioinformatics databases.

import os
import sys
import urllib.request
import urllib.parse

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_olis.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

# Helper functions for various bioinformatics databases

def fetch_uniprot(accession):
    """Fetch protein FASTA from UniProt."""
    url = f"https://www.uniprot.org/uniprot/{accession}.fasta"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode('utf-8')

def fetch_ncbi_fasta(accession, db='nucleotide'):
    """Fetch FASTA from NCBI Entrez."""
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    params = urllib.parse.urlencode({'db': db, 'id': accession, 'rettype': 'fasta', 'retmode': 'text'})
    url = f"{base}efetch.fcgi?{params}"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode('utf-8')

def solve(data):
    # For demonstration: interpret input as an accession ID and fetch its sequence
    accession = data.strip()
    if accession:
        try:
            # Try UniProt first (protein accessions are typically alphanumeric)
            result = fetch_uniprot(accession)
            print(result)
        except Exception:
            try:
                result = fetch_ncbi_fasta(accession)
                print(result)
            except Exception as e:
                print(f"Could not fetch {accession}: {e}", file=sys.stderr)

if __name__ == '__main__':
    solve(get_input())
