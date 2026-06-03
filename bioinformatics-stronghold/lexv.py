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
    import io, contextlib
    path = 'rosalind-inputs/bioinformatics-stronghold/rosalind_lexv.txt'
    use_file = os.path.exists(path)
    text = open(path).read() if use_file else sys.stdin.read()
    lines = text.strip().splitlines()
    alphabet = lines[0].split()
    n = int(lines[1])
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        print('\n'.join(lexv(alphabet, n)))
    output = buf.getvalue()
    sys.stdout.write(output)
    if use_file:
        out_path = 'rosalind-outputs/bioinformatics-stronghold/rosalind_lexv.txt'
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(output)


if __name__ == '__main__':
    main()
