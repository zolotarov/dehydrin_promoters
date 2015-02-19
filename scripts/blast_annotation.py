"""
This script will take a protein FASTA file and find top 10 hits in the
non-redundant proteint database using NCBI BLAST. Will return the evalue, the
accession and the description of the hits.

This script takes quite a long time and often interrupts, due to NCBI not 
responding in the alloted time. Has to be restarted several times when 
350 sequences were analyzed, removing the sequences for which the results were
obtained.

Run as:
python blast_annotation.py proteins.faa > output.tab
"""

from Bio import SeqIO
from Bio import SearchIO
from Bio.Blast import NCBIWWW
from sys import argv

sequences = open(argv[1], 'r')

for sequence in SeqIO.parse(sequences, "fasta"):
    result_handle = NCBIWWW.qblast("blastp", "nr", str(sequence.seq),
                                   hitlist_size=10, expect=1e-03)
    save_file = open("my_blast.xml", "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()
    blast_qresult = SearchIO.read('my_blast.xml', 'blast-xml')
    for i in range(0, len(blast_qresult)):
        blast_hsp = blast_qresult[i][0]
        evalue = blast_hsp.evalue
        desc = blast_hsp.hit_description
        hit_id = blast_hsp.hit_id
        print sequence.id, '\t', evalue, '\t', hit_id, '\t', desc
