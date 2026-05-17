#	Computing GC Content

def parse_fasta(lines):
    sequences = {}
    current_id = None
    current_seq = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        if line.startswith(">"):
            if current_id is not None:
                sequences[current_id] = "".join(current_seq)
            current_id = line[1:]
            current_seq = []
        else:
            current_seq.append(line)

    if current_id is not None:
        sequences[current_id] = "".join(current_seq)

    return sequences


def gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    return (g_count + c_count) / len(sequence) * 100


with open("C:/Users/user/Documents/Python_code/Rosalind_code/rosalind_files/rosalind_gc.txt", "r") as file_handle:
    lines = file_handle.readlines()

sequences = parse_fasta(lines)

best_id = None
best_gc = -1.0

for seq_id, seq in sequences.items():
    gc = gc_content(seq)
    if gc > best_gc:
        best_gc = gc
        best_id = seq_id

print(best_id)
print(f"{best_gc:.6f}")
