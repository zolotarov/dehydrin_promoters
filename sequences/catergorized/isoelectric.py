from sys import argv
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# p = ProteinAnalysis('MAGNPGMRDGYGSDIRRAEEHVGGHTQKNDHLMVFPTFGQSEDDGQGGRRKKKSVKDKITEKLPGGKGSEKHGRTEYVHQEVHHEPEKKGMMDKIKEKLPGGHHTEEHSHAGSTVHHEVHHETHHDHEKKGMMEKLMEKLPGHH')
# print p.isoelectric_point()
for seq in SeqIO.parse(open(argv[1], "r"), "fasta"):
    pi = ProteinAnalysis(str(seq.seq)).isoelectric_point()
    if pi < 7.0:
    	print pi, "acidic", seq.id.split('|')[0]
    else:
    	print pi, "basic", seq.id.split('|')[0]





