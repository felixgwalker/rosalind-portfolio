#	Complimenting a Strand of DNA

dna_str = 'AAAACCCGGT'
comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
rev_comp =('')

for nuc in dna_str:
	rev_comp += comp[nuc]

rev_comp = rev_comp[::-1]

print(rev_comp)

# rev_comp2 = ''.join(comp[nuc] for nuc in dna_str)[::-1]	


message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)