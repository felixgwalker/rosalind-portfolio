# Finding a Most Likely Common Ancestor (rosalind_cons)

with open(r"c:\Users\user\Documents\python_code\Rosalind_code\rosalind_files\rosalind_cons.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]

sequences = []
current_sequence = []

for line in lines:
    if line.startswith(">"):
        if current_sequence:
            sequences.append("".join(current_sequence))
            current_sequence = []
    else:
        current_sequence.append(line)

if current_sequence:
    sequences.append("".join(current_sequence))

n = len(sequences[0])

profile = {base: [0] * n for base in "ACGT"}

for seq in sequences:
    for i, base in enumerate(seq):
        profile[base][i] += 1

consensus = "".join(max("ACGT", key=lambda b: profile[b][i]) for i in range(n))

print(consensus)
for base in "ACGT":
    print(f"{base}: {' '.join(map(str, profile[base]))}")
