"""
Given a dehydrin CDS FASTA file, and a k-segs FASTA file
output the CDS of just the K-segment
"""

from Bio import SeqIO
from Bio.Seq import Seq
from sys import argv

k_segs = list()
for rec in SeqIO.parse(open('../k-segs.fas', 'r'), 'fasta'):
	k_segs.append(str(rec.seq))

k_segs = set(k_segs)

all_recs = list()
for rec in SeqIO.parse(open(argv[1], 'r'), 'fasta'):
	for x in range(0, len(str(rec.seq)) - 45 + 1, 3):
		seg = Seq(str(rec.seq)[x:x+45])
		if str(seg.translate()) in k_segs:
			id = rec.id.split('|')[0]
			all_recs.append(id)
			print ">%s_%d" % (id, all_recs.count(id))
			print seg

# print all_recs, len(set(all_recs))

# for gene in set(all_recs):
# 	print gene
