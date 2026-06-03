# Inferring Genotype from a Pedigree (MEND)
# Rosalind problem: https://rosalind.info/problems/mend/
#
# Problem: Given a Newick pedigree tree where leaves are labeled with
# genotypes (AA, Aa, or aa), compute the probability distribution
# (P(AA), P(Aa), P(aa)) for the root individual.
#
# Interpretation: each internal node (including root) is the offspring of
# its two Newick "children" (the convention in this problem is parent = child
# in Newick sense).  Probabilities propagate bottom-up via Mendel's laws.
#
# Formula:
#   Let pA = P(A allele transmitted from parent) = P(AA) + P(Aa)/2
#   P(offspring=AA) = pA1 × pA2
#   P(offspring=aa) = (1−pA1) × (1−pA2)
#   P(offspring=Aa) = 1 − P(AA) − P(aa)

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_mend.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def parse_newick(s):
    """Returns (root, children_dict) where leaves are genotype strings."""
    s = s.strip().rstrip(';')
    children = {}
    counter = [0]

    def new_node():
        counter[0] += 1
        return f'__n{counter[0]}'

    def parse(pos):
        if pos < len(s) and s[pos] == '(':
            pos += 1
            kids = []
            while True:
                child, pos = parse(pos)
                kids.append(child)
                if pos < len(s) and s[pos] == ',':
                    pos += 1
                else:
                    break
            pos += 1  # ')'
            lb = pos
            while pos < len(s) and s[pos] not in '(),;':
                pos += 1
            label = s[lb:pos].strip() or new_node()
            children[label] = kids
            return label, pos
        else:
            lb = pos
            while pos < len(s) and s[pos] not in '(),;':
                pos += 1
            label = s[lb:pos].strip()
            children.setdefault(label, [])
            return label, pos

    root, _ = parse(0)
    return root, children

GENO_PROB = {
    'AA': (1.0, 0.0, 0.0),
    'Aa': (0.0, 1.0, 0.0),
    'aa': (0.0, 0.0, 1.0),
}

def combine(p1, p2):
    """Compute offspring genotype distribution from two parent distributions."""
    pA1 = p1[0] + p1[1] / 2
    pA2 = p2[0] + p2[1] / 2
    aa_prob  = (1 - pA1) * (1 - pA2)
    AA_prob  = pA1 * pA2
    Aa_prob  = 1 - AA_prob - aa_prob
    return (AA_prob, Aa_prob, aa_prob)

def solve(data):
    root, children = parse_newick(data.strip())

    memo = {}

    def prob(node):
        if node in memo:
            return memo[node]
        kids = children[node]
        if not kids:
            # Leaf: genotype label
            result = GENO_PROB.get(node, (1/3, 1/3, 1/3))
        else:
            p1 = prob(kids[0])
            p2 = prob(kids[1])
            result = combine(p1, p2)
        memo[node] = result
        return result

    AA, Aa, aa = prob(root)
    print(f'{AA:.3f} {Aa:.3f} {aa:.3f}')

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
