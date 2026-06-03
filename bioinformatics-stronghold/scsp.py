# Interleaving Two Motifs (SCSP) — Shortest Common Supersequence
# Rosalind problem: https://rosalind.info/problems/scsp/
#
# Problem: Given two DNA strings s and t (each ≤ 1000 nt), find their shortest
# common supersequence — the shortest string that has both s and t as subsequences.
#
# Key identity: |SCS(s,t)| = |s| + |t| - |LCS(s,t)|
# We compute LCS first, then reconstruct the SCS by interleaving the two strings
# while keeping the LCS characters "shared".
#
# Algorithm: LCS DP then SCS reconstruction. O(|s|·|t|) time and space.

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-inputs', 'bioinformatics-stronghold', 'rosalind_scsp.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip(), path.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def shortest_common_supersequence(s, t):
    m, n = len(s), len(t)
    # Build LCS DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct SCS by tracing back through the DP table
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            # Characters match: include once (shared in LCS)
            result.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            # Came from s
            result.append(s[i-1])
            i -= 1
        else:
            # Came from t
            result.append(t[j-1])
            j -= 1

    # Append remaining characters
    while i > 0:
        result.append(s[i-1])
        i -= 1
    while j > 0:
        result.append(t[j-1])
        j -= 1

    return ''.join(reversed(result))

def solve(data):
    lines = data.splitlines()
    s, t = lines[0].strip(), lines[1].strip()
    print(shortest_common_supersequence(s, t))

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
