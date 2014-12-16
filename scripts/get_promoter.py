from Bio import SeqIO
from sys import argv
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../database/dehydrins.db')
conn = engine.connect()

command = """SELECT gene, species, peptide_seq from GENES 
			 WHERE latest="Yes" AND use="Yes" AND promoter_seq!="None"
	  """

results = conn.execute(command)

for row in results:
	gene = row[0]
	species = row[1]
	promoter_seq = row[2]

	print ">{0}|{1}\n{2}".format(gene,species,promoter_seq)
