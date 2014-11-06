from sys import argv
from Bio import SeqIO
from Bio.Seq import Seq

motif = Seq("CCGAC")

counter = 0
for record in SeqIO.parse(open(argv[1], 'r'), 'fasta'):
	if motif in record.seq or motif.reverse_complement() in record.seq:
		counter += 1

print counter
