from Bio import SeqIO
from Bio.Alphabet import IUPAC
from sys import argv
import random


out_filename = str(argv[1]).split('.')[0] + "_oneline.fas"

with open(out_filename, "w") as out_file:
        for record in SeqIO.parse(argv[1], "fasta"):
                rec_id = ">" + str(record.id).split('|')[0] + "\n"
                seq = str(record.seq) + "\n"
                if "Sequenceunavailable" in record.seq:
                        continue
                elif "R" in seq:
                	seq = seq.replace('R', random.choice('AG'))
                elif "Y" in seq:
                	seq = seq.replace('Y', random.choice('CT'))
                elif "S" in seq:
                	seq = seq.replace('S', random.choice('GC'))
                elif "W" in seq:
                	seq = seq.replace('W', random.choice('AT'))
                elif "K" in seq:
                	seq = seq.replace('K', random.choice('GT'))	
                elif "M" in seq:
                	seq = seq.replace('M', random.choice('AC'))
                elif "B" in seq:
                	seq = seq.replace('B', random.choice('CGT'))
                elif "D" in seq:
                	seq = seq.replace('D', random.choice('AGT'))
                elif "H" in seq:
                	seq = seq.replace('H', random.choice('ACT'))
                elif "V" in seq:
                	seq = seq.replace('V', random.choice('ACG'))
                else:
                        out_file.write(rec_id)
                        out_file.write(seq)
