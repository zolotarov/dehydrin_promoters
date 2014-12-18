from sys import argv

gene_list = [line.split('\t') for line in open(argv[1], 'r')]
species_list = [line.split('\t')[0] for line in open (argv[2], 'r')]

species_dict = dict()

for species in species_list:
	species_abbrev = species.split()[0][0]+species.split()[1]
	species_dict[species_abbrev] = species

print species_dict

for gene in gene_list:
	# gene = gene.strip().split('\t')
	print species_dict[gene[1]], '\t', gene[0], '\t', gene[2].strip()
