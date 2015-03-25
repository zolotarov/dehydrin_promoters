#!/usr/bin/python
# -*- coding: utf-8 -*-
from Bio import AlignIO, Motif, SeqIO
from Bio.Alphabet import IUPAC

import re

alphabet = IUPAC.protein


def pwm_maker(alignment_file):
    alignment = AlignIO.read(alignment_file, 'fasta', alphabet=alphabet)
    m = Motif.Motif(alphabet)
    for a in alignment:
        m.add_instance(a.seq)
    return m

# files contain the alignment of motifs that was created previously using pwm_?_seg.py
y_m = pwm_maker('../sequences/y-segs.fas')  
k_m = pwm_maker('../sequences/k-segs.fas')

# KS_dehydrins = open('../sequences/KS_dehydrins.faa', 'w')
# YnSKn_dehydrins = open('../sequences/YnSKn_dehydrins.faa', 'w')
# Kn_dehydrins = open('../sequences/Kn_dehydrins.faa', 'w')
# SKn_dehydrins = open('../sequences/SKn_dehydrins.faa', 'w')
# YnKn_dehydrins = open('../sequences/YnKn_dehydrins.faa', 'w')
# uncategorized_dehydrins = open('../sequences/uncategorized_dehydrins.faa', 'w')

for record in SeqIO.parse('../sequences/all_deh_peptides.faa', 'fasta',
                          alphabet=alphabet):

     # dictionary for each sequence that uses position as keys, since the position is unique 
     # and segement type (K, Y, S) as values

    segments = dict()

    K_segs = [pos for (pos, score) in k_m.search_pwm(record.seq,
              threshold=5.0, both=False) if score >= 10]

    Y_segs = [pos for (pos, score) in y_m.search_pwm(record.seq,
              threshold=5.0, both=False) if score >= 10]
    

    # find the S segments that are a sequence of Serines 4 or longer or SSSGS or SSSDS

    S_segs = [result.start() for result in
              re.finditer('[S]{4,}|[S]{3}[D|G][S]', str(record.seq))]
    if Y_segs == []:
        Y_segs = '-'
    if S_segs ==[]:
        S_segs = '-'
    print record.id, '\t', K_segs, '\t', Y_segs, '\t', S_segs
