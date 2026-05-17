# Shortening the Motif Search (KMP Failure Array)

def parse_fasta(text):
    lines = text.strip().splitlines()
    seq = []
    for line in lines:
        if not line.startswith('>'):
            seq.append(line.strip())
    return ''.join(seq)

def failure_array(s):
    n = len(s)
    P = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and s[k] != s[i]:
            k = P[k - 1]
        if s[k] == s[i]:
            k += 1
        P[i] = k
    return P

with open(r'c:\Users\user\Documents\python_code\Rosalind_code\rosalind_files\rosalind_kmp.txt') as f:
    fasta_input = f.read()

s = parse_fasta(fasta_input)
result = failure_array(s)
print(' '.join(map(str, result)))
