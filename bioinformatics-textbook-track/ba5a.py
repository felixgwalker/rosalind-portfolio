# BA5A — Find the Minimum Number of Coins Needed to Make Change
# https://rosalind.info/problems/ba5a/
#
# Given: an integer money and a list of coin denominations.
# Return: the minimum number of coins needed.
# Classic DP: dp[m] = min coins to make change for m.

import os, sys

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-inputs', 'bioinformatics-textbook-track', 'rosalind_ba5a.txt')
    if os.path.exists(p):
        return open(p).read().strip(), p.replace('rosalind-inputs', 'rosalind-outputs')
    return sys.stdin.read().strip(), None

def solve(data):
    lines = data.splitlines()
    money = int(lines[0].strip())
    coins = list(map(int, lines[1].split(',')))
    dp = [float('inf')] * (money + 1)
    dp[0] = 0
    for m in range(1, money + 1):
        for c in coins:
            if m >= c and dp[m-c] + 1 < dp[m]:
                dp[m] = dp[m-c] + 1
    print(dp[money])

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
