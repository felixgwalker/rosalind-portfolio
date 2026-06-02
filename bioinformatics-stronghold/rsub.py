# Identifying Reversing Substitutions (RSUB)
# Rosalind problem: https://rosalind.info/problems/rsub/
#
# Problem: Given a rooted binary tree (Newick) with DNA sequences at each
# leaf (FASTA), reconstruct ancestral sequences via the Fitch parsimony
# algorithm, then count the total number of "reversing substitutions" across
# all alignment positions — pairs of edges (e1, e2) on the same root-to-leaf
# path where the character changes from X→Y at e1 and then back Y→X at e2.
#
# Algorithm:
#   1. Fitch bottom-up to find character sets at each internal node.
#   2. Fitch top-down to assign a single character to each internal node.
#   3. For each position, for each node pair (anc, desc) where anc is a proper
#      ancestor of desc: if char(parent(anc))==char(desc) and char(anc)!=char(parent(anc)),
#      that is a reversing substitution on that root-to-leaf path segment.
#      Equivalently: walk root-to-leaf; whenever X→Y→…→X occurs, record one reversal
#      per time the original X is recovered.

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_rsub.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return sys.stdin.read()

def parse_newick(s):
    s = s.strip().rstrip(';')
    children, parent = {}, {}
    counter = [0]

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
            pos += 1
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
    root, children, parent = parse_newick(blocks[0].strip())
    leaf_seqs = parse_fasta('\n\n'.join(blocks[1:]))

    # Post-order traversal
    order = []
    def postorder(v):
        for c in children[v]:
            postorder(c)
        order.append(v)
    postorder(root)

    seq_len = len(next(iter(leaf_seqs.values())))

    # Fitch bottom-up
    fitch_sets = {}
    for v in order:
        if not children[v]:
            fitch_sets[v] = [frozenset(leaf_seqs[v][p]) for p in range(seq_len)]
        else:
            c1, c2 = children[v]
            node_sets = []
            for p in range(seq_len):
                inter = fitch_sets[c1][p] & fitch_sets[c2][p]
                node_sets.append(inter if inter else fitch_sets[c1][p] | fitch_sets[c2][p])
            fitch_sets[v] = node_sets

    # Fitch top-down assignment
    assigned = {}
    for v in reversed(order):
        if not children[v]:
            assigned[v] = leaf_seqs[v]
            continue
        chars = []
        for p in range(seq_len):
            if v not in parent:
                ch = min(fitch_sets[v][p])
            else:
                pc = assigned[parent[v]][p]
                ch = pc if pc in fitch_sets[v][p] else min(fitch_sets[v][p])
            chars.append(ch)
        assigned[v] = ''.join(chars)

    # Count reversing substitutions
    # For each root-to-leaf path, scan for X→Y→X patterns
    total = 0
    leaves_list = [v for v in order if not children[v]]

    for leaf in leaves_list:
        # Build path from root to leaf
        path = []
        v = leaf
        while v is not None:
            path.append(v)
            v = parent.get(v)
        path.reverse()  # root first

        for p in range(seq_len):
            seq = [assigned[node][p] for node in path]
            # Count reversals: find pairs i < j where seq[i-1] == seq[j] and seq[i] != seq[i-1]
            # where edge i is (path[i-1], path[i]) and edge j is (path[j-1], path[j])
            for i in range(1, len(seq)):
                if seq[i] != seq[i-1]:  # substitution at edge i
                    original = seq[i-1]
                    for j in range(i+1, len(seq)):
                        if seq[j-1] != seq[j]:  # another substitution at edge j
                            if seq[j] == original:  # reversion back to original
                                total += 1

    print(total)

if __name__ == '__main__':
    solve(get_input())
