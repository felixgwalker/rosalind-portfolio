# GenBank Introduction (GBK)
# Rosalind problem: https://rosalind.info/problems/gbk/
#
# Problem: Access the NCBI GenBank database via the Entrez API to count how
# many GenBank records for a given taxon were published in a given date range.
#
# Input: genus name, date1, date2
# Output: count of GenBank nucleotide records
#
# Requires internet access to NCBI Entrez API.
# Uses urllib (standard library) — no BioPython.

import os
import sys
import urllib.request
import urllib.parse
import json

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_gbk.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

ENTREZ_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def esearch(db, term):
    """Search NCBI Entrez and return the count of results."""
    params = urllib.parse.urlencode({
        'db': db,
        'term': term,
        'rettype': 'count',
        'retmode': 'json'
    })
    url = f"{ENTREZ_BASE}esearch.fcgi?{params}"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    return int(data['esearchresult']['count'])

def solve(data):
    lines = data.splitlines()
    genus = lines[0].strip()
    date1 = lines[1].strip()   # YYYY/MM/DD
    date2 = lines[2].strip()   # YYYY/MM/DD

    # Build an Entrez search query: organism + date range
    term = f'"{genus}"[Organism] AND {date1}[PDAT]:{date2}[PDAT]'
    try:
        count = esearch('nucleotide', term)
        print(count)
    except Exception as e:
        print(f"Error fetching from NCBI: {e}", file=sys.stderr)
        print(0)

if __name__ == '__main__':
    solve(get_input())
