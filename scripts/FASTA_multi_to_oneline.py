from Bio import SeqIO
from sys import argv

out_filename = str(argv[1]).split('.')[0] + "_oneline.fas"

with open(out_filename, "w") as out_file:
	for record in SeqIO.parse(argv[1], "fasta"):
		rec_id = ">" + str(record.id).split('|')[0] + "\n"
		seq = str(record.seq) + "\n"
		out_file.write(rec_id)
		out_file.write(seq)
