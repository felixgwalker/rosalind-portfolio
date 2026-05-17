#	Finding a Motif in DNA

with open("C:/Users/user/Documents/Python_code/Rosalind_code/rosalind_files/rosalind_subs.txt", "r") as file:
    dna_sequence = file.readline().strip()
    motif = file.readline().strip()

motif_length = len(motif)
positions = []

for start_index in range(len(dna_sequence) - motif_length + 1):
    substring = dna_sequence[start_index : start_index + motif_length]

    if substring == motif:
        positions.append(start_index + 1)

print(" ".join(map(str, positions)))
