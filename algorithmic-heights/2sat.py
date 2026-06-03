# 2-Satisfiability (2SAT)
# Rosalind problem: https://rosalind.info/problems/2sat/
#
# Problem: Given a 2-CNF formula with n variables and m clauses, determine if
# it is satisfiable and output a satisfying assignment, or output 0 if not.
# Each clause (a OR b) adds implications: (NOT a → b) and (NOT b → a).
# Algorithm: Build implication graph, find SCCs with Kosaraju's. The formula is
# UNSAT iff any variable x and NOT x are in the same SCC. Otherwise x is TRUE
# when SCC(x) appears later than SCC(NOT x) in topological order. O(n + m).

import os
import sys
from collections import defaultdict

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'algorithmic-heights', 'rosalind_2sat.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    n, m = map(int, lines[0].split())

    # Literal encoding: variable x (1-indexed) → index x-1; NOT x → index x-1+n
    def lit(x):
        return x - 1 if x > 0 else -x - 1 + n

    adj = defaultdict(list)
    radj = defaultdict(list)

    for line in lines[1:m+1]:
        a, b = map(int, line.split())
        # Clause (a OR b) → (NOT a → b) and (NOT b → a)
        for u_lit, v_lit in [(lit(-a), lit(b)), (lit(-b), lit(a))]:
            adj[u_lit].append(v_lit)
            radj[v_lit].append(u_lit)

    total = 2 * n
    visited = [False] * total
    order = []

    def dfs1(start):
        stack = [(start, False)]
        while stack:
            u, done = stack.pop()
            if done:
                order.append(u)
                continue
            if visited[u]:
                continue
            visited[u] = True
            stack.append((u, True))
            for v in adj[u]:
                if not visited[v]:
                    stack.append((v, False))

    for i in range(total):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * total
    scc_id = 0

    def dfs2(start, cid):
        stack = [start]
        while stack:
            u = stack.pop()
            if comp[u] != -1:
                continue
            comp[u] = cid
            for v in radj[u]:
                if comp[v] == -1:
                    stack.append(v)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, scc_id)
            scc_id += 1

    result = []
    for i in range(n):
        if comp[i] == comp[i + n]:
            print(0)
            return
        # Variable is TRUE when its SCC is topologically later (higher scc_id)
        result.append(1 if comp[i] > comp[i + n] else 0)

    print(1)
    print(' '.join(map(str, result)))

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
