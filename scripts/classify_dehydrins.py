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

KS_dehydrins = open('../sequences/KS_dehydrins.faa', 'w')
YnSKn_dehydrins = open('../sequences/YnSKn_dehydrins.faa', 'w')
Kn_dehydrins = open('../sequences/Kn_dehydrins.faa', 'w')
SKn_dehydrins = open('../sequences/SKn_dehydrins.faa', 'w')
YnKn_dehydrins = open('../sequences/YnKn_dehydrins.faa', 'w')
uncategorized_dehydrins = open('../sequences/uncategorized_dehydrins.faa', 'w')

for record in SeqIO.parse('../sequences/all_dehydrins.faa', 'fasta',
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

    for position in K_segs:
        segments[position] = 'K'

    for position in Y_segs:
        segments[position] = 'Y'

    # since there is only one S segment per sequence, if the list is not empty, 
    # the first item is saved into the dictionary

    if S_segs != []:
        segments[int(S_segs[0])] = 'S'
    else:
        pass

    # segment_sequence is list of all segment types in the order of their position in the amino
    # acid sequence
    segment_sequence = [segments[key] for key in
                        sorted(segments.iterkeys())]

    # a string of dehydrin type, e.g. Y2SK2, KS or S2K, if the segment occurs once, then the 
    # number of occurences is ommited
    dehydrin_classification = ''.join((str(letter)
            + str(segment_sequence.count(letter)) if segment_sequence.count(letter)
            > 1 else letter) for letter in set(segment_sequence))

    print record.id, dehydrin_classification

    if re.search('KS', dehydrin_classification):
        SeqIO.write(record, KS_dehydrins, 'fasta')
    elif re.search('Y[1-9]SK[1-9]',dehydrin_classification):
        SeqIO.write(record, YnSKn_dehydrins, 'fasta')
    elif re.search('Y[1-9]K[1-9]',dehydrin_classification):
        SeqIO.write(record, YnKn_dehydrins, 'fasta')
    elif re.search('SK[1-9]',dehydrin_classification):
        SeqIO.write(record, SKn_dehydrins, 'fasta')
    elif re.search('^K[1-9]',dehydrin_classification):
        SeqIO.write(record, Kn_dehydrins, 'fasta') # none of this type are found in my set
    else:
        SeqIO.write(record, uncategorized_dehydrins, 'fasta')

KS_dehydrins.close()
YnSKn_dehydrins.close()
Kn_dehydrins.close()
SKn_dehydrins.close()
YnKn_dehydrins.close()
uncategorized_dehydrins.close()