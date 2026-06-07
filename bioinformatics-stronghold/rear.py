# Reversal Distance (REAR)
# Rosalind problem: https://rosalind.info/problems/rear/
#
# Problem: Given 5 pairs of permutations (each of {1,...,n}, n ≤ 10), compute
# the reversal distance for each pair — the minimum number of reversals
# (of contiguous sub-sequences) needed to transform the first into the second.
#
# Algorithm: Bidirectional BFS, alternately expanding a frontier from the source
# and a frontier from the target, treating each reachable permutation as a state.
# The first permutation found in both frontiers gives the distance (sum of the
# depths reached on each side). Searching from both ends keeps the explored
# state count roughly the square root of single-direction BFS, which is what
# makes n = 10 (10! = 3.6M states, ~45 reversals per state) tractable in Python.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_rear.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def neighbors(perm):
    """All permutations reachable from perm via a single reversal."""
    n = len(perm)
    perm_list = list(perm)
    for i in range(n):
        for j in range(i + 1, n):
            yield tuple(perm_list[:i] + perm_list[i:j+1][::-1] + perm_list[j+1:])

def reversal_distance(src, tgt):
    """Bidirectional BFS for the minimum reversals transforming src into tgt."""
    if src == tgt:
        return 0
    front_src = {src: 0}
    front_tgt = {tgt: 0}
    frontier_src = [src]
    frontier_tgt = [tgt]
    while frontier_src and frontier_tgt:
        # Expand the smaller frontier first to minimize work.
        if len(frontier_src) <= len(frontier_tgt):
            frontier, own, other = frontier_src, front_src, front_tgt
        else:
            frontier, own, other = frontier_tgt, front_tgt, front_src
        next_frontier = []
        depth = own[frontier[0]] + 1
        for perm in frontier:
            for new_perm in neighbors(perm):
                if new_perm in other:
                    return depth + other[new_perm]
                if new_perm not in own:
                    own[new_perm] = depth
                    next_frontier.append(new_perm)
        if frontier is frontier_src:
            frontier_src = next_frontier
        else:
            frontier_tgt = next_frontier
    return -1   # should never reach here for valid input

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    results = []
    i = 0
    while i < len(lines):
        src = tuple(map(int, lines[i].split()))
        tgt = tuple(map(int, lines[i+1].split()))
        results.append(reversal_distance(src, tgt))
        i += 2
    print(' '.join(map(str, results)))

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
