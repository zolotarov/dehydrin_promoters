import subprocess

no_blast_genes = ['Gorai.007G257100|Graimondii', 'Lus10003340.g|Lusitatissimum', 'Lus10022643.g|Lusitatissimum']
with open('supplemental_table.csv', 'r') as suppl:
	suppl.readline()
	for line in suppl:
		line = line.strip().split(',')
		new_line = []
		for item in line:
			item = item.strip()
			new_line.append(item)
		
		species_split = new_line[0].split()
		abbrev_species = species_split[0][0]+species_split[1]
		gene_name = "{0}|{1}".format(new_line[1], abbrev_species)
		if gene_name in no_blast_genes:
			grep_seg = subprocess.check_output(["grep", gene_name, "segment_positions.tab"])
			seg_split = grep_seg.split('\t')[1:]
			K_seg = seg_split[0].translate(None, "[]").split(',')
			K_seg = ",".join(K_seg)
			Y_seg = seg_split[1].translate(None, "[]").split(',')
			Y_seg = ",".join(Y_seg)
			S_seg = seg_split[2].translate(None, "[]").strip()
			print new_line[0], '\t', new_line[1], '\t', new_line[2], "-", '\t', "-", '\t', "-", '\t', K_seg, '\t', Y_seg, '\t', S_seg
		else:
			grep_result = subprocess.check_output(["grep", gene_name, "all_deh_results.tab"])
			grep_seg = subprocess.check_output(["grep", gene_name, "segment_positions.tab"])
			grep_split = grep_result.split('\n')[0].split('\t')
			evalue = grep_split[1]
			accession = grep_split[2].split('|')[3]
			description = grep_split[3].split(">")[0]
			grep_seg = subprocess.check_output(["grep", gene_name, "segment_positions.tab"])
			seg_split = grep_seg.split('\t')[1:]
			K_seg = seg_split[0].translate(None, "[]").split(',')
			K_seg = ",".join(K_seg)
			Y_seg = seg_split[1].translate(None, "[]").split(',')
			Y_seg = ",".join(Y_seg)
			S_seg = seg_split[2].translate(None, "[]").strip()
			print new_line[0], '\t', new_line[1], '\t', new_line[2], '\t', evalue, '\t', accession, '\t', description, '\t', K_seg, '\t', Y_seg, '\t', S_seg
