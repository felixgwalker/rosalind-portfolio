# Sorting by Reversals (SORT)
# Rosalind problem: https://rosalind.info/problems/sort/
#
# Problem: Given two permutations of {1,...,n} (n <= 10), find the minimum
# number of reversals (of contiguous sub-sequences) needed to transform the
# first into the second, and output that count followed by one "i j" pair
# (1-indexed, inclusive endpoints) per reversal in the sequence applied.
#
# Algorithm: Bidirectional BFS over the permutation graph (edges = single
# reversals). Each side records, for every permutation it reaches, the parent
# permutation and the reversal that connects them; reversals are involutions,
# so the same edge is traversed in reverse on the other side. When the two
# frontiers meet at a permutation M, the path src -> ... -> M -> ... -> tgt is
# reconstructed by walking the parent pointers from M back to src (reversed)
# and from M forward to tgt.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_sort.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def neighbors_with_op(perm):
    """Yield (new_perm, (i, j)) for every single reversal of perm[i..j]."""
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            yield perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:], (i, j)

def reversal_path(src, tgt):
    """Bidirectional BFS returning the list of (i, j) reversals taking src to tgt."""
    if src == tgt:
        return []
    # parent_f[perm] = (prev, op): applying op to prev yields perm (prev is closer to src)
    # parent_b[perm] = (next, op): applying op to perm yields next (next is closer to tgt)
    parent_f = {src: None}
    parent_b = {tgt: None}
    frontier_f = [src]
    frontier_b = [tgt]
    meeting = None
    while meeting is None:
        if len(frontier_f) <= len(frontier_b):
            frontier, own, other, forward = frontier_f, parent_f, parent_b, True
        else:
            frontier, own, other, forward = frontier_b, parent_b, parent_f, False
        next_frontier = []
        for perm in frontier:
            for new_perm, op in neighbors_with_op(perm):
                if new_perm not in own:
                    own[new_perm] = (perm, op)
                    if new_perm in other:
                        meeting = new_perm
                        break
                    next_frontier.append(new_perm)
            if meeting is not None:
                break
        if forward:
            frontier_f = next_frontier
        else:
            frontier_b = next_frontier

    ops_to_meeting = []
    node = meeting
    while parent_f[node] is not None:
        prev, op = parent_f[node]
        ops_to_meeting.append(op)
        node = prev
    ops_to_meeting.reverse()

    ops_from_meeting = []
    node = meeting
    while parent_b[node] is not None:
        nxt, op = parent_b[node]
        ops_from_meeting.append(op)
        node = nxt

    return ops_to_meeting + ops_from_meeting

def solve(data):
    lines = [l.strip() for l in data.splitlines() if l.strip()]
    src = tuple(map(int, lines[0].split()))
    tgt = tuple(map(int, lines[1].split()))
    ops = reversal_path(src, tgt)
    print(len(ops))
    for i, j in ops:
        print(f"{i + 1} {j + 1}")

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
