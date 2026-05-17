# Concensus and Profile

with open("input.txt", "r") as file:
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

sequence_length = len(sequences[0])

profile = {
    "A": [0] * sequence_length,
    "C": [0] * sequence_length,
    "G": [0] * sequence_length,
    "T": [0] * sequence_length,
}

for dna_sequence in sequences:
    for position, base in enumerate(dna_sequence):
        profile[base][position] += 1

consensus = []

for position in range(sequence_length):
    counts = {
        "A": profile["A"][position],
        "C": profile["C"][position],
        "G": profile["G"][position],
        "T": profile["T"][position],
    }

    most_common_base = max(counts, key=counts.get)
    consensus.append(most_common_base)

print("".join(consensus))

for base in "ACGT":
    print(base + ": " + " ".join(map(str, profile[base])))


