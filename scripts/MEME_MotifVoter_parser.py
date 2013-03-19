from sys import argv
import re

# second argument is the original promoter file
with open(argv[2], 'r') as promoter_file:
	names = [line.strip().split('>')[1] for line in promoter_file if ">" in line]
names_dict = dict((name[0:24], number) for number, name in enumerate(names))


input_file = open(argv[1], 'r').read()

for m in re.finditer('MOTIF.+\d{3}', input_file):
    motif_n = (m.group(0)).split('\t')[0]
    e_value = (m.group(0)).split('E-value = ')[-1]

    if float(e_value) <= 5e-2:
        motifs = input_file.split(motif_n)[1].split('sites sorted by position p-value')[1].split('--------------------------------------------------------------------------------')[1].split('\n')[3:]
        consensus = input_file.split(motif_n)[1].split('sites sorted by position p-value')[0].split('Multilevel')[1].split('\n')[0].strip()
        print ('\n' + "MOTIF FINDER: MEME")
    	print "MOTIF:", consensus
    	print "INSTANCES:"
        for motif in motifs:
        	if motif:
	        	name = motif.split(' ')[0].split('|')[0]
	        	if name:
	        		seq_number = names_dict[motif.split(' ')[0].split('|')[0]]
	        	
	        	direction = re.search("\s+[+|-]\s+", motif).group(0).strip()
	        	location = -(int(re.search("\s+\d+\s+", motif).group(0).strip())) if direction == '-' else (-1000 + int(re.search("\s+\d+\s+", motif).group(0).strip()) - 1)
	        	
	        	
	        	to_print = str(names_dict[name]) + ',' + str(
            location) + ',' + consensus + ',' + direction
	        	print to_print