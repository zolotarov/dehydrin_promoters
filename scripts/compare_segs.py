from Bio import SeqIO

new_seg = SeqIO.parse(open("y-segs_new.txt", "r"), "fasta")
old_seg = SeqIO.parse(open("../sequences/y-segs.fas", "r"), "fasta")

new_seq = []
old_seq = []

for record in new_seg:
	new_seq.append(str(record.seq))

for record in old_seg:
	old_seq.append(str(record.seq))

print set(new_seq)-set(old_seq)

print set(old_seq) -set(new_seq)
