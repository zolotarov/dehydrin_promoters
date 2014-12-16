from subprocess import check_output
import os
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from sys import argv

os.environ['IUPred_PATH'] = "/home/yzolotarov/iupred"


prot_seqs = SeqIO.parse(argv[1], "fasta")

def iupred_score(sequence):
    """
    http://iupred.enzim.hu/
    The Pairwise Energy Content Estimated from Amino Acid Composition 
    Discriminates between Folded and Intrinsically Unstructured Proteins 
    Zsuzsanna Dosztanyi, Veronika Csizmok, Peter Tompa and Istvan Simon 
    J. Mol. Biol. (2005) 347, 827-839.
    """
    with open('temp.fas', 'w') as temp_out:
        temp_out.write(">temp_seq\n")
        temp_out.write(sequence)
    res = check_output(["/home/yzolotarov/iupred/iupred", 
    "/home/yzolotarov/dehydrin_promoters/scripts/temp.fas", "long"])
    res = res.split('\n')
    scores = [float(line.split()[2]) for line in res[:-1] if '#' not in line]
    disordered = [s for s in scores if s >= 0.5]
    return float(len(disordered))/len(scores)

def aroma(sequence):
    aromaticity = ProteinAnalysis(sequence).aromaticity()
    return aromaticity

def aliphatic(sequence):
    """ includes the aliphatic index followed by amino acid percent values
    """
    percent = ProteinAnalysis(sequence).get_amino_acids_percent()
    aliphatic_index = percent['A'] + 2.9 * percent['V'] + 3.9 * (percent['I']
        + percent['L'])
    return aliphatic_index

def gravy(sequence):
    if 'X' or '*' in sequence:
        sequence = sequence.replace('X', '')
        sequence = sequence.replace('*', '')
        g = ProteinAnalysis(sequence).gravy()
    else:
        g = ProteinAnalysis(sequence).gravy()
    return g


for record in prot_seqs:
    # print record.id, '\t', iupred_score(str(record.seq))
    print record.id, '\t', iupred_score(str(record.seq)), '\t', aroma(str(record.seq)), '\t', aliphatic(str(record.seq)), '\t', gravy(str(record.seq))

