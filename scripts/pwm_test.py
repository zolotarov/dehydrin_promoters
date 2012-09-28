from Bio import AlignIO, Motif, SeqIO
from Bio.Alphabet import IUPAC
from Bio.Motif.Thresholds import ScoreDistribution 
from sys import argv
script, proteins = argv
alphabet = IUPAC.protein
alignment = AlignIO.read("k-segs7.fas", "fasta", alphabet=alphabet)
m = Motif.Motif(alphabet)
all_segments = list()
for a in alignment:
    m.add_instance(a.seq)
    all_segments.append("%s" % a.seq) 
    
output_deh = open("dehydrins_search.txt", "w")
ksegs_new = open("k-segs_new.txt", "w")
dehydrin_fas = open("dehydrins.fas", "w")
print m.format("transfac")

