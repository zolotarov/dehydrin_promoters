all_species = []
with open('all_dehydrins.faa', 'r') as file:
	for line in file:
		line = line.strip()
		if line[0] == '>':
			species = line.split('|')[-1]
			all_species.append(species)

all_sp = set(all_species)

print len(all_sp)
for i in all_sp:
	print "%s." % i[0], i[1:]