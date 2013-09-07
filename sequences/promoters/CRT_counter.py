from Bio import SeqIO

seqs = SeqIO.parse(open('KS_with_oxytropis.fas', 'r'), 'fasta')

for sequence in seqs:
	if "CCGAC" in sequence.seq or "GTCGG" in sequence.seq:
		print sequence.id