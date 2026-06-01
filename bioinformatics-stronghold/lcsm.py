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
    path = 'rosalind-files/rosalind_lcsm.txt'
    text = open(path).read() if os.path.exists(path) else sys.stdin.read()
    print(lcsm(parse_fasta(text)))


if __name__ == '__main__':
    main()
