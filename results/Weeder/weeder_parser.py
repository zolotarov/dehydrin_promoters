"""
Parser for Weeder de novo motif analysis results, returns a position frequency
matrix that can be then used by MATLIGN. Use .wee file as input
Only the "most interesting highest highest-ranking" motifs are considered.
Example output that can be directly pasted to MATLIGN
(http://ekhidna.biocenter.helsinki.fi/poxo/matlign/matlign):

A C G T

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
from Bio import motifs


def bracket_check(motif):
    if '[' in motif or ']' in motif:
        return None
    else:
        return motif

with open(argv[1], 'r') as input_file:
    contents = input_file.read().split(
        '*** Interesting motifs (highest-ranking) seem to be :')[1].split(
            '*** Interesting motifs (not highest-ranking) can also be :'
            )[0].split('Best occurrences:')[1:]
    for item in contents:
        print ">matrix"
        item = filter(None, item.split('match')[1].split(
            'Frequency Matrix')[0].split('\n')[:-1])
        motif_list = [filter(None, i.split(
            ' '))[2] for i in item if '[' not in i]
        # print motifs

        m = motifs.create(motif_list)
        trans = m.format("transfac")

        for l in trans.split('\n')[1:-3]:
            numbers = filter(None, l.split(' '))[1:-1]
            print (' '.join(numbers))
