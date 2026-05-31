# Searching Datasets Globally (GREP)
# Rosalind problem: https://rosalind.info/problems/grep/
#
# Problem: Search the NCBI protein database for proteins in a given taxon.
# Given: a protein substring (motif) and a taxon.
# Return: the number of proteins in that taxon containing the motif.
#
# Uses NCBI Entrez API to search the protein database.

import os
import sys
import urllib.request
import urllib.parse
import json

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_grep.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

ENTREZ_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def entrez_search_count(db, term):
    params = urllib.parse.urlencode({'db': db, 'term': term, 'rettype': 'count', 'retmode': 'json'})
    url = f"{ENTREZ_BASE}esearch.fcgi?{params}"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    return int(data['esearchresult']['count'])

def solve(data):
    lines = data.splitlines()
    motif = lines[0].strip()
    taxon = lines[1].strip() if len(lines) > 1 else 'Homo sapiens'
    term = f'"{motif}"[Feature Key] AND "{taxon}"[Organism]'
    try:
        count = entrez_search_count('protein', term)
        print(count)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    solve(get_input())
