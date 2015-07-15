from Bio import SeqIO
import re
from sys import argv

CRT = r"CCGAC|GTCGG"
REa = r"AACCAA|TTGGTT"

# seq = "TGCTTTGGAGCGTGGATCATGTGGTGCTAGCCATTCTCATTCACATCCTCATTATGATGATGATTTGGATGAAGAGTCACTTGATGGCGATAATTGATCTTATTATGGTTACTTGTTGGATGGCAAAACACTTGATATTTTGTAGTTTCAAGACTATGTTATATTTTGTAGTTGATTATGTTATATTTTGTAGTTTCAAGAATGTTTTGTTTTATGCTGTGGTGTTTTGAGATTAAGCATTCTGATATGGTATTTTGTTTCATTACTATCTTTTGGCCTGTTCTAGGAGTAGTGTTAGTAAAGGGACAAACTAAATGTATTAGGAGCAGTGGTAGAAATGAAAAGTAGGAAAATTAATTAAAAAAAAAATCGTATTTTAGCGTCGGCCACCCCAACGCTATGATTGTTGACCATTTTCGTTGACTAATTAGCGTCCGTCCATCCGACGCTATATATGTTGACTAAATTTCATTGACTAAATAGCGTCCGTCTATCCCCAACGCTGGATTGGGCCAAAACCCCACCCAAGTGTTGTGGGGTTTTGGCCCAGTCTGAAACACCTTCTGGTCAAACTCTAAATTAATTAGAACTCGTTTTCCCTAAACATAGAAGTGGATCAAAGACCTCTTAAAAAAGAAGCCCCCATTTTACCTAAGGTGAATATAGGTACAAGATAATTAACTTTACAAAAATAATGCATGCGTTATCGGATTAAGTGTACCTAACAATTTGAACTCATGCTTTGCTGGTTTGCTTAATGGCCATATATACTTTTTTTCATAAAAAAACAATATACATTTAACACGTAGTGTACACGTTCATGGTCATTCTTGTAATTTCCACAAAAGTTGTGGATAACATTTTATATTAATATATCTCTACTTTCTCGACCTTGTGATTCACAATCTCTTTCTATAAATACCATTGATCATTCCCTTCAAATTCATATCAAACCACATCCAAAACCAAAACAAAACACAAGGAAAAACCAATCAACAAT"
for record in SeqIO.parse(argv[1], 'fasta'):
	if re.search(CRT, str(record.seq)) and re.search(REa, str(record.seq)):
		print record.id

# if re.search(CRT, seq):
# 	print "YES"