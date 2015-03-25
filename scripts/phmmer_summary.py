"""
Measure frequency of dehydrin annotation in phmmer_description.tab
"""

from sys import argv
import re

# create a list of regular expression that contain possible dehydrin synonyms
# for every synonym InterPro and Pfam databases were used to confirm that it
# is a dehydrin
dehydrin_synonyms = ['.*dehydrin.*', '.*Dehydrin.*', '.*AT1G20440.*',
					 '.*ERD10C.*', '.*LEA.*', '.*Cold acclimation.*',
					 '.*Paf93.*', '.*COR410.*', '.*WZY1-2.*', '.*Dhn.*',
					 '.*COR15.*', '.*cold acclimation.*', '.*Cold stress.*',
					 '.*Dehydrative stress.*', '.*ECPP44.*', '.*TAS14.*',
					 '.*Sb03g032255.*', '.*Late embryogenesis.*', '.*Rab21.*',
					 '.*At4g38410.*', '.*Cold shock protein CS66.*',
					 '.*DHN.*', '.*Cold-stress.*', '.*Sb10g003700.*',
					 '.*Sb04g032250.*', '.*At1g54410.*', '.*RAB17.*',
					 '.*Dehydration-stress.*', '.*Water stress.*', 
					 '.*Cold-inducible.*', '.*cold-regulated.*', '.*bdn1.*',
					 '.*Abscisic acid response.*', '.*Cor 15.*', '.*CAS15.*',
					 '.*Cold-acclimation specific protein 15.*', '.*Lea.*',
					 '.*Abscisic acid response.*', '.*Lea2.*', '.*Cor29.*',
					 '.*Pollen coat.*', '.*Putative cold-regulated protein.*',
					 '.*Cold-acclimation specific.*', '.*CPRD22.*',
					 '.*Desiccation-related protein clone PCC6-19.*',
					 '.*Putative RAB protein.*', '.*Cold-regulated.*',
					 '.*Putative cold-regulated.*', '.*Dehydration protein.*',
					 '.*Cold-shock protein CS120.*']

with open(argv[1], 'r') as phmmer_in:
	phmmer_dict = {}
	for line in phmmer_in:
		line = line.strip().split('\t')
		phmmer_dict[line[0]] = line[1:]

combine_synonyms = "(" + ")|(".join(dehydrin_synonyms) + ")"

for gene in phmmer_dict:
	dehydrin_counter = 0
	for description in phmmer_dict[gene]:
		if re.match(combine_synonyms, description):
			dehydrin_counter += 1
	if dehydrin_counter < 5:
		print gene, dehydrin_counter

