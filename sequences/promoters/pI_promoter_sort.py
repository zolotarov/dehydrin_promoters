from Bio import SeqIO
from sys import argv

genes = list()
with open(argv[2], "r") as pi_file:
	for line in pi_file:
		line = line.strip()
		genes.append(line)

# print genes

for seq in SeqIO.parse(open(argv[1], "r"), "fasta"):
	if seq.id.split('|')[0] in genes:
		print ">" + str(seq.id)
		print seq.seq
