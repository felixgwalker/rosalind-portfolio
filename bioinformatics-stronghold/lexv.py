import sys
import os


def lexv(alphabet, n):
    results = []

    def dfs(s):
        if s:
            results.append(s)
        if len(s) < n:
            for c in alphabet:
                dfs(s + c)

    dfs('')
    return results


def main():
    path = 'rosalind-files/rosalind_lexv.txt'
    text = open(path).read() if os.path.exists(path) else sys.stdin.read()
    lines = text.strip().splitlines()
    alphabet = lines[0].split()
    n = int(lines[1])
    print('\n'.join(lexv(alphabet, n)))


if __name__ == '__main__':
    main()
