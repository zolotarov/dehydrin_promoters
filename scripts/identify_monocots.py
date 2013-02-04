from Bio import SeqIO
monocots = ["Sbicolor", "Zmays", "Sitalica", "Pvirgatum", "Osativa", "Bdistachyon"]

dehydrins_monocots = open("dehydrins_monocots.faa", "w")
dehydrins_dicots = open("dehydrins_dicots.faa", "w'")
for record in SeqIO.parse("dehydrins.fas", "fasta"):
	if record.id.split('|')[2] in monocots:
		SeqIO.write(record, dehydrins_monocots, "fasta")
	else:
		SeqIO.write(record, dehydrins_dicots, "fasta")

dehydrins_monocots.close()
dehydrins_dicots.close()
