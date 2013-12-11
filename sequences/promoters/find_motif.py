from Bio import SeqIO
from Bio.Seq import Seq
from sys import argv

file = argv[1]
motif = Seq(argv[2])

all_occurences =[]
for record in SeqIO.parse(open(file, 'r'), 'fasta'):
	if str(motif) in record.seq or motif.reverse_complement() in record.seq:
		all_occurences.append(record.id)

all_occurences = set(all_occurences)
print len(all_occurences)

