from Bio import SeqIO

species_codes = {"Acoerulea": "AC",
				"Alyrata": "AL",
				"Athaliana": "AT",
				"Bdistachyon": "BD",
				"Cclementina": "CC",
				"Cpapaya": "CP",
				"Crubella": "CR",
				"Csativus": "CA",
				"Csinensis": "CS",
				"Egrandis": "EG",
				"Gmax": "GM",
				"Lusitatissimum": "LU",
				"Mdomestica": "MD",
				"Mesculenta": "ME",
				"Mguttatus": "MG",
				"Mtruncatula": "MT",
				"Osativa": "OS",
				"Ppersica": "PP",
				"Ptrichocarpa": "PT",
				"Pvulgaris": "PV",
				"Rcommunis": "RC",
				"Sbicolor": "SB",
				"Sitalica": "SI",
				"Thalophila": "TH",
				"Vvinifera": "VV",
				"Zmays": "ZM"}

records = list(SeqIO.parse("../sequences/SKn_dehydrins_promoters.fas", "fasta"))

command_line = ""
for record in records:
	species_name = record.id.split('|')[-1]
	if species_name in species_codes:
		command_line += species_codes[species_name]

print command_line
