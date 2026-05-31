# PDB Introduction (PDBT)
# Rosalind problem: https://rosalind.info/problems/pdbt/
#
# Problem: Given a PDB accession ID, fetch the structure file and count the
# number of residues in a specified chain that have an alpha-carbon (CA) atom.
# Input: PDB ID and chain ID
# Output: number of CA-containing residues in that chain
#
# Fetches PDB data from RCSB PDB via HTTP.

import os
import sys
import urllib.request

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_pdbt.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def fetch_pdb(pdb_id):
    """Fetch PDB file as text from RCSB."""
    url = f"https://files.rcsb.org/download/{pdb_id.upper()}.pdb"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode('utf-8', errors='replace')

def count_ca_residues(pdb_text, chain_id):
    """Count distinct residue numbers in chain that have a CA atom."""
    residues = set()
    for line in pdb_text.splitlines():
        if line.startswith('ATOM') or line.startswith('HETATM'):
            atom_name = line[12:16].strip()
            chain = line[21].strip()
            res_num = line[22:26].strip()
            if chain == chain_id and atom_name == 'CA':
                residues.add(res_num)
    return len(residues)

def solve(data):
    lines = data.splitlines()
    pdb_id = lines[0].strip()
    chain_id = lines[1].strip() if len(lines) > 1 else 'A'
    try:
        pdb_text = fetch_pdb(pdb_id)
        count = count_ca_residues(pdb_text, chain_id)
        print(count)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    solve(get_input())
