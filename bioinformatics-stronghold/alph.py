# Alignment-Based Phylogeny (ALPH)
# Rosalind problem: https://rosalind.info/problems/alph/
#
# Problem: Given a rooted binary tree (Newick) and DNA sequences for each
# leaf (FASTA), find the minimum-parsimony score and the ancestral sequences
# at internal nodes using the Fitch algorithm.
#
# Algorithm (Fitch small parsimony):
#   Bottom-up pass: at each internal node, if the intersection of children's
#   character sets is non-empty take it (cost 0); otherwise take the union
#   (cost +1 = one substitution on some edge).
#   Top-down pass: assign a concrete character to each internal node consistent
#   with the bottom-up sets (prefer the parent's character if it is in the set).
#
# Output: parsimony score, then the tree in Newick form with internal-node
# sequences labelled.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_alph.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_newick(s):
    s = s.strip().rstrip(';')
    children = {}
    parent   = {}
    counter  = [0]

    def new_node():
        counter[0] += 1
        return f'__n{counter[0]}'

    def parse(pos):
        if s[pos] == '(':
            pos += 1
            kids = []
            while True:
                child, pos = parse(pos)
                kids.append(child)
                if s[pos] == ',':
                    pos += 1
                else:
                    break
            pos += 1  # ')'
            lb = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[lb:pos].strip() or new_node()
            if s[pos:pos+1] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            children[label] = kids
            for c in kids:
                parent[c] = label
            return label, pos
        else:
            lb = pos
            while pos < len(s) and s[pos] not in '(),;:':
                pos += 1
            label = s[lb:pos].strip()
            if s[pos:pos+1] == ':':
                pos += 1
                while pos < len(s) and s[pos] not in '(),;':
                    pos += 1
            children.setdefault(label, [])
            return label, pos

    root, _ = parse(0)
    return root, children, parent

def parse_fasta(text):
    seqs, cur, parts = {}, None, []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            if cur:
                seqs[cur] = ''.join(parts)
            cur, parts = line[1:].split()[0], []
        else:
            parts.append(line)
    if cur:
        seqs[cur] = ''.join(parts)
    return seqs

def solve(data):
    blocks = data.strip().split('\n\n')
    newick_line = blocks[0].strip()
    fasta_text  = '\n'.join(blocks[1:])

    root, children, parent = parse_newick(newick_line)
    leaf_seqs = parse_fasta(fasta_text)

    # Topological order (post-order)
    order = []
    def postorder(v):
        for c in children[v]:
            postorder(c)
        order.append(v)
    postorder(root)

    leaves  = [v for v in order if not children[v]]
    seq_len = len(next(iter(leaf_seqs.values())))

    # Bottom-up Fitch
    sets   = {}  # node -> list of frozenset per position
    score  = 0
    for v in order:
        if not children[v]:
            sets[v] = [frozenset(leaf_seqs[v][p]) for p in range(seq_len)]
        else:
            c1, c2 = children[v]
            node_sets = []
            for p in range(seq_len):
                inter = sets[c1][p] & sets[c2][p]
                if inter:
                    node_sets.append(inter)
                else:
                    node_sets.append(sets[c1][p] | sets[c2][p])
                    score += 1
            sets[v] = node_sets

    # Top-down assignment
    assigned = {}
    for v in reversed(order):
        if not children[v]:
            assigned[v] = leaf_seqs[v]
            continue
        seq_chars = []
        for p in range(seq_len):
            if v not in parent:
                ch = min(sets[v][p])
            else:
                par_ch = assigned[parent[v]][p]
                ch = par_ch if par_ch in sets[v][p] else min(sets[v][p])
            seq_chars.append(ch)
        assigned[v] = ''.join(seq_chars)

    print(score)
    # Output Newick with internal node sequences as labels
    def to_newick(v):
        if not children[v]:
            return f'{v}'
        c1, c2 = children[v]
        return f'({to_newick(c1)},{to_newick(c2)}){assigned[v]}'
    print(to_newick(root) + ';')

if __name__ == '__main__':
    solve(get_input())
