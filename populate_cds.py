from Bio import SeqIO
from sys import argv
from sqlalchemy import create_engine

file = argv[1]

# for record in SeqIO.parse(open(file, 'r'), 'fasta'):
# 	print record.id.split('|')[0], record.seq


engine = create_engine('sqlite:///database/dehydrins.db')
conn = engine.connect()

for record in SeqIO.parse(open(file, 'r'), 'fasta'):
	gene_id = record.id.split('|')[0].split()[0]
	cds = str(record.seq)
	conn.execute("""UPDATE genes SET coding_seq='%s'
	                WHERE transcript='%s'""" % (cds, gene_id))
	print "Inserted %s" % gene_id