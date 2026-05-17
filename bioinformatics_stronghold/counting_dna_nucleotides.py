#	Counting DNA Nucleotides

dna_str = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
tmpFreqDict = {'A':0, 'T':0, 'G':0, 'C':0}
for nuc in dna_str:
	tmpFreqDict[nuc] += 1

print(tmpFreqDict['A'], tmpFreqDict['C'], tmpFreqDict['G'], tmpFreqDict['T'])