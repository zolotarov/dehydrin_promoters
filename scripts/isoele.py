from Bio import SeqIO
from sys import argv
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database/dehydrins.db')
conn = engine.connect()

command = """SELECT gene, peptide_seq, promoter_seq from GENES where latest='Yes'
		  """

results = conn.execute(command)

for row in results:
	gene = row[0]
	peptide_seq = row[1]
	promoter_seq = row[2]
	pi = ProteinAnalysis(str(peptide_seq)).isoelectric_point()
	if pi > 7.0:
		print ">{0}\n{1}".format(gene,promoter_seq)

