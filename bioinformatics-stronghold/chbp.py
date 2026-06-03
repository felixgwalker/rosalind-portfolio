# Character-Based Phylogeny (CHBP)
# Rosalind problem: https://rosalind.info/problems/chbp/
#
# Problem: Given n taxa and m binary characters (each a 0/1 string of length n),
# either output a phylogenetic tree consistent with all characters using the
# perfect-phylogeny algorithm, or output "-1" if no such tree exists.
#
# Two binary characters are COMPATIBLE iff not all four patterns (00, 01, 10,
# 11) appear simultaneously across any pair of taxa — the "four-gametes" test.
#
# Algorithm:
#   1. Check all C(m,2) pairs of characters for compatibility.
#   2. If any pair is incompatible, output -1.
#   3. Otherwise, build the tree recursively: find a character that splits the
#      current taxon set, recurse on each half with remaining characters.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_chbp.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def compatible(c1_vals, c2_vals):
    """Return True iff the two binary character arrays are compatible."""
    patterns = set()
    for v1, v2 in zip(c1_vals, c2_vals):
        patterns.add((v1, v2))
        if len(patterns) == 4:
            return False
    return True

def build_tree(taxa, char_indices, char_matrix):
    """Recursively build a Newick string for the given taxa subset."""
    if len(taxa) == 1:
        return taxa[0]
    if not char_indices:
        return '(' + ','.join(sorted(taxa)) + ')'

    for ci in char_indices:
        grp0 = [t for t in taxa if char_matrix[t][ci] == '0']
        grp1 = [t for t in taxa if char_matrix[t][ci] == '1']
        if grp0 and grp1:
            remaining = [c for c in char_indices if c != ci]
            left  = build_tree(grp0, remaining, char_matrix)
            right = build_tree(grp1, remaining, char_matrix)
            return f'({left},{right})'

    # All characters identical for this group — return as polytomy
    return '(' + ','.join(sorted(taxa)) + ')'

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    taxa = lines[0].split()
    n = len(taxa)
    # Characters: each subsequent line is a binary string of length n
    chars = [lines[i+1] for i in range(len(lines) - 1)]
    m = len(chars)

    # Build character matrix: char_matrix[taxon][char_index] = '0' or '1'
    char_matrix = {}
    for t_idx, t in enumerate(taxa):
        char_matrix[t] = [chars[ci][t_idx] for ci in range(m)]

    # Check compatibility of all pairs
    for i in range(m):
        for j in range(i + 1, m):
            c1 = [char_matrix[t][i] for t in taxa]
            c2 = [char_matrix[t][j] for t in taxa]
            if not compatible(c1, c2):
                print(-1)
                return

    tree = build_tree(taxa, list(range(m)), char_matrix)
    print(tree + ';')

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
