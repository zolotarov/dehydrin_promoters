from Bio import AlignIO, Motif, SeqIO
from Bio.Alphabet import IUPAC
# from Bio.Motif.Thresholds import ScoreDistribution 
# from sys import argv
# script, proteins = argv
alphabet = IUPAC.protein
alignment = AlignIO.read("../sequences/selected_Y-segs.fas", "fasta", alphabet=alphabet)
m = Motif.Motif(alphabet)
all_segments = list()
for a in alignment:
    m.add_instance(a.seq)
    all_segments.append("%s" % a.seq) 
    
output_deh = open("dehydrins_search_y.txt", "w")
ysegs_new = open("y-segs_new.txt", "w")
#dehydrin_fas = open("dehydrins.fas", "w")
print m.format("transfac")

# count = 0
# for member in all_segments:
# 	count +=1
# print count

#print m.log_odds()
#m.weblogo("Motif.png")

print m.max_score()
print m.min_score()
#print m
# print all_segments
# print m.exp_score(st_dev = True) # prints expected score and standard deviation

records_saved = list()
for record in SeqIO.parse("../sequences/all_dehydrins.faa", "fasta", alphabet=alphabet):
# 	for pos, seq in m.search_instances(record.seq):
# 		continue

	for pos, score in m.search_pwm(record.seq, threshold=5.0, both=False):
		if score >= 14:
			line =  ">" + str(record.id) + "\t" + str(pos) + "\t" + str(record.seq[pos:pos+7]) + "\t" + str(score) + "\n"
			output_deh.write(line)
			defline = ">" + str(record.id) + "\n"
			y_seg = str(record.seq[pos:pos+7]) + "\n"
		#	if record.id not in records_saved:
		#		SeqIO.write(record, dehydrin_fas, "fasta")
	#			records_saved.append(record.id)
			if str(record.seq[pos:pos+7]) not in all_segments:
				ysegs_new.write(defline)
				ysegs_new.write(y_seg)
		else:
			continue

output_deh.close()
ysegs_new.close()
#dehydrin_fas.close()
