from sys import argv
import numpy as np
from Bio import motifs

name = str(argv[1]).split('.')[0]
name_pfm = name + '.pfm'
name_transfac = name + '.transfac'
mat = np.genfromtxt(argv[1])
mat_trans = mat.transpose()

t = ''
for i in range(len(mat_trans)):
	for j in  mat_trans[i]:
		t += str(int(j))
		t += ' '
	t += '\n'

with open(name_pfm, 'w') as pfm_out:
	pfm_out.write(t)

mot = motifs.read(open(name_pfm), 'pfm')
print mot.format("transfac")

# with open(name_transfac, 'w') as transfac_out:
# 	transfac_out.write(mot.format("transfac"))
