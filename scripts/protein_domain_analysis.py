"""
This scripts takes BLAST hits and get domain information from NCBI
BLAST hits are produced by blast_annotation.py
"""


from sys import argv
import subprocess
from collections import defaultdict
import cPickle
import time

file_out = open("res_out.pkl", "w")

with open(argv[1], 'r') as input_file:
    results = defaultdict(list)
    for line in input_file:
        line = line.strip().split('\t')
        gene_name = line[0].split('|')[0]
        protein_match = line[2].split('|')[3]
        esearch_out = subprocess.Popen(["esearch", "-db", "protein", "-query",
                        "{}".format(protein_match)], stdout=subprocess.PIPE)
        efetch_out = subprocess.Popen(["efetch", "-format", "xml"],
                        stdin=esearch_out.stdout, stdout=subprocess.PIPE)
        xtract_out = subprocess.check_output(["xtract", "-element",
                        "SeqFeatData_region"], stdin=efetch_out.stdout)
        results[gene_name].append(xtract_out)
        print gene_name, '\t', xtract_out
        file_out = open("res_out.pkl", "w")
        cPickle.dump(results, file_out)
        file_out.close()
        time.sleep(5)

file_out.close()

