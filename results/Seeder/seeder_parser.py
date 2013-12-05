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

with open(argv[1], 'r') as input_file:
    contents = input_file.read().split('Q-value(')[1:]
    for item in contents:
        evalue = item.split('Information Content')[0].split('=')[1].strip()
        if float(evalue) < 0.01:
            print ">matrix", float(evalue)
            motif = item.split('>NFM')[1].split('>PWM')[0].split('\n')[3:-2]
            nfm = [' '.join(filter(None, m.split(' ')[1:])) for m in motif]
            for i in nfm:
                print i
