import sys
import os


def parse_fasta(text):
    seqs = []
    current = []
    for line in text.strip().splitlines():
        if line.startswith('>'):
            if current:
                seqs.append(''.join(current))
                current = []
        else:
            current.append(line.strip())
    if current:
        seqs.append(''.join(current))
    return seqs


def lcsm(seqs):
    shortest = min(seqs, key=len)
    lo, hi = 1, len(shortest)
    best = ''
    while lo <= hi:
        mid = (lo + hi) // 2
        found = None
        for i in range(len(shortest) - mid + 1):
            sub = shortest[i:i + mid]
            if all(sub in s for s in seqs):
                found = sub
                break
        if found:
            best = found
            lo = mid + 1
        else:
            hi = mid - 1
    return best


def main():
    import io, contextlib
    path = 'rosalind-inputs/bioinformatics-stronghold/rosalind_lcsm.txt'
    use_file = os.path.exists(path)
    text = open(path).read() if use_file else sys.stdin.read()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        print(lcsm(parse_fasta(text)))
    output = buf.getvalue()
    sys.stdout.write(output)
    if use_file:
        out_path = 'rosalind-outputs/bioinformatics-stronghold/rosalind_lcsm.txt'
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(output)


if __name__ == '__main__':
    main()
