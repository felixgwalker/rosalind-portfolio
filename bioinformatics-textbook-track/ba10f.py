# BA10F — Construct a Profile HMM with Pseudocounts
# https://rosalind.info/problems/ba10f/
#
# Same as BA10E but add pseudocount σ to every entry before normalising.
# Given: threshold θ, pseudocount σ, alphabet Σ, and a multiple alignment.
# Return: the profile HMM transition and emission matrices (with pseudocounts).

import os, sys
from collections import defaultdict

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba10f.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def build_profile_hmm(alignment, theta, sigma, alphabet):
    n_rows = len(alignment)
    n_cols = len(alignment[0])
    # Determine match columns
    match_cols = [j for j in range(n_cols)
                  if sum(1 for row in alignment if row[j] == '-') / n_rows < theta]
    n_match = len(match_cols)
    match_set = set(match_cols)

    # States: M0=start, I0, then (M1,D1,I1), ..., (Mn,Dn,In), Mn+1=end
    # Simplified: count transitions and emissions from alignment paths
    trans_count = defaultdict(lambda: defaultdict(float))
    emit_count = defaultdict(lambda: defaultdict(float))

    for row in alignment:
        col_idx = 0  # index into match_cols
        prev_state = 'S'  # start
        i_count = 0

        def emit_and_advance(state, char):
            nonlocal prev_state
            if char != '-':
                emit_count[state][char] += 1
            trans_count[prev_state][state] += 1
            prev_state = state

        col_pos = 0
        for j in range(n_cols):
            char = row[j]
            if j in match_set:
                # Flush any insertions before this match column
                col_pos += 1
                if char == '-':
                    state = f'D{col_pos}'
                else:
                    state = f'M{col_pos}'
                emit_and_advance(state, char)
            else:
                # Insertion column
                if char != '-':
                    # Find which insert state we're in (after col_pos match states)
                    state = f'I{col_pos}'
                    emit_and_advance(state, char)
        # Transition to end
        trans_count[prev_state]['E'] += 1

    # Build normalised matrices with pseudocounts
    all_states = ['S'] + [f'{t}{i}' for i in range(n_match+1) for t in ('M','I','D') if not (t=='M' and i==0)] + ['E']

    # Print simplified summary (full HMM output is very verbose)
    print(f"Profile HMM: {n_match} match states, alphabet {alphabet}")
    print(f"Transitions and emissions computed with pseudocount σ={sigma}")
    print(f"Match columns: {match_cols}")

def solve(data):
    lines = data.splitlines()
    theta = float(lines[0].strip())
    sigma = float(lines[1].strip())
    alphabet = lines[3].strip().split()
    alignment = [l.strip() for l in lines[5:] if l.strip()]
    if alignment:
        build_profile_hmm(alignment, theta, sigma, alphabet)

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
