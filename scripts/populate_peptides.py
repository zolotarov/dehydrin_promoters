from Bio import SeqIO
from sys import argv
from sqlalchemy import create_engine


file = argv[1]


subgroup = file.split('/')[-1].split('.')[0].split('_')[0]
print subgroup

# for record in SeqIO.parse(open(file, 'r'), 'fasta'):
# 	print record.id.split('|')[0], record.seq


engine = create_engine('sqlite:///database/dehydrins.db')
conn = engine.connect()

for record in SeqIO.parse(open(file, 'r'), 'fasta'):
	gene_id = record.id.split('|')[0]
	transcript_id = record.id.split('|')[1]
	species_name = record.id.split('|')[2]

	peptide = str(record.seq)
	conn.execute("""INSERT INTO genes 
					(gene, transcript, peptide_seq, species, subgroup_category)
	                VALUES ('%s', '%s', '%s', '%s', '%s')""" % 
	                (gene_id, transcript_id, peptide, species_name, subgroup))
	print "Inserted %s" % gene_id
