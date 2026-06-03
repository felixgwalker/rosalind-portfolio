# BA5M — Find a Highest-Scoring Multiple Sequence Alignment
# https://rosalind.info/problems/ba5m/
#
# Given: three DNA strings. Return: the score and a multiple alignment using
# a 3D DP (match=+1 when all three agree, gap=-1 per gap column character).

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba5m.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    s, t, u = lines[0].strip(), lines[1].strip(), lines[2].strip()
    l, m, n = len(s), len(t), len(u)
    GAP = -1
    # 3D DP
    dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l+1)]
    for i in range(l+1):
        for j in range(m+1):
            for k in range(n+1):
                if i==0 and j==0 and k==0: continue
                candidates = []
                if i>0 and j>0 and k>0:
                    match = 1 if s[i-1]==t[j-1]==u[k-1] else 0
                    candidates.append(dp[i-1][j-1][k-1]+match)
                if i>0 and j>0: candidates.append(dp[i-1][j-1][k]+GAP)
                if i>0 and k>0: candidates.append(dp[i-1][j][k-1]+GAP)
                if j>0 and k>0: candidates.append(dp[i][j-1][k-1]+GAP)
                if i>0: candidates.append(dp[i-1][j][k]+GAP)
                if j>0: candidates.append(dp[i][j-1][k]+GAP)
                if k>0: candidates.append(dp[i][j][k-1]+GAP)
                dp[i][j][k] = max(candidates) if candidates else 0
    print(dp[l][m][n])

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
