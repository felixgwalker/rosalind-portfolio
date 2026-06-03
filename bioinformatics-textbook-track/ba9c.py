# BA9C — Construct the Suffix Tree of a String
# https://rosalind.info/problems/ba9c/
#
# Given: a string. Return: the edge labels of its suffix tree (one per line).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba9c.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

class SuffixTree:
    def __init__(self, s):
        self.s = s; self.root = {}
        for i in range(len(s)):
            self._insert(s[i:])
    def _insert(self, suffix):
        node = self.root
        while suffix:
            first = suffix[0]
            if first not in node:
                node[first] = [suffix, {}]; return
            edge_label, child = node[first]
            k = 0
            while k < len(edge_label) and k < len(suffix) and edge_label[k] == suffix[k]:
                k += 1
            if k == len(edge_label):
                node = child; suffix = suffix[k:]
            else:
                shared = edge_label[:k]; rest_e = edge_label[k:]; rest_s = suffix[k:]
                new_child = {rest_e[0]: [rest_e, child]}
                node[first] = [shared, new_child]
                if rest_s: new_child[rest_s[0]] = [rest_s, {}]
                return

def collect(node, result):
    for ch, (label, child) in node.items():
        result.append(label); collect(child, result)

def solve(data):
    s = data.strip()
    st = SuffixTree(s + '$')
    edges = []; collect(st.root, edges)
    for e in edges: print(e)

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
