"""
Parser for MEME de novo motif analysis results, returns a position frequency 
matrix that can be then used by MATLIGN.
Only motifs with e-value below 0.05 are considered significant.
Example output that can be directly pasted to MATLIGN 
(http://ekhidna.biocenter.helsinki.fi/poxo/matlign/matlign):

>matrix
0 7 17 2
0 16 5 5
0 24 0 2
0 0 0 26
24 0 2 0
0 0 0 26
26 0 0 0
26 0 0 0
26 0 0 0
0 0 0 26

"""

from sys import argv
from Bio import motifs  # BioPython 1.61+ is required
# from Bio.Seq import Seq

with open(argv[1], 'r') as input_file:
    contents = input_file.read().split('E-value')[2:]
    lines = '-' * 80
    stars = '*' * 80

    for item in contents:
        evalue = float(item.split(stars)[0].strip().split('=')[1].strip())
        # print item
        # print evalue
        if evalue <= 0.05:
            list_of_motifs = item.split('sites sorted by position p-value')[
                1].split(lines)[1].split('----------')[2].strip()
            # print list_of_motifs
            print ">matrix", evalue

            motif_list = []
            for line in list_of_motifs.split('\n'):
                line_list = filter(None, line.split(' '))
                motif_list.append(line_list[-2])
            # print motif_list

            m = motifs.create(motif_list)
            trans = m.format("transfac")
            # print trans

            for l in trans.split('\n')[1:-3]:
                numbers = filter(None, l.split(' '))[1:-1]
                print (' '.join(numbers))
