from Bio import SeqIO
from sys import argv
monocots = ["Pdactylifera", "Sbicolor", "Zmays", "Sitalica", "Pvirgatum", "Osativa", "Bdistachyon"]

mono_file = str(argv[1]).split('.')[0] + "_mono.fas"
print str(argv[1]).split('.')
di_file = str(argv[1]).split('.')[0] + "_di.fas"
dehydrins_monocots = open(mono_file, "w")
dehydrins_dicots = open(di_file, "w'")
for record in SeqIO.parse(argv[1], "fasta"):
	if record.id.split('|')[-1] in monocots:
		SeqIO.write(record, dehydrins_monocots, "fasta")
	else:
		SeqIO.write(record, dehydrins_dicots, "fasta")

dehydrins_monocots.close()
dehydrins_dicots.close()
