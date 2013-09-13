from sys import argv
from collections import defaultdict

dehydrin_count = defaultdict(int)

# with open("species.md", 'r') as sp:
# 	for line in sp:
# 		line = line.strip()


with open(argv[1], 'r') as f:
	for line in f:
		if '>' == line[0]:
			species = line.strip().split("|")[-1]
			dehydrin_count[species] += 1


for name in sorted(dehydrin_count.keys()):
	print name, '\t', dehydrin_count[name]


