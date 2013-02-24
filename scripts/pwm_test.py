from Bio import AlignIO, Motif
from Bio.Alphabet import IUPAC

alphabet = IUPAC.protein

alignment = AlignIO.read("../sequences/k-segs.fas", "fasta", alphabet=alphabet)

m = Motif.Motif(alphabet)
all_segments = list()
for a in alignment:
    m.add_instance(a.seq)
    all_segments.append("%s" % a.seq) 
    
m.weblogo("Motif.png")
print m.format("transfac")