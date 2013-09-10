"""
Count the occurence of a motif and its reverse complement
Provide the file name as the first argument and the motif as the second
e.g.: python KS_dehydrins.fas CCGAC
"""

from Bio import SeqIO
from Bio.Seq import Seq
from sys import argv

seqs = SeqIO.parse(open(argv[1], 'r'), 'fasta')
motif = Seq(argv[2])
number_seqs = 0
counter = 0

for sequence in seqs:
	number_seqs += 1
	if motif in sequence.seq or motif.reverse_complement() in sequence.seq:
		counter += 1
		print sequence.id

print "Total number of promoters with motif %s: %d/%d" % (motif, counter, number_seqs) 