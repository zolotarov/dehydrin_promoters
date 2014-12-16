"""
Run this in docs dir to get lists of all proteins
awk {'print $1,$2'} species.md|while read line

do
genus=`awk {'print $1'} <<< $line`
species=`awk {'print $2'} <<< $line`
whole="$genus-$species.txt"
esearch -db protein -query "$genus $species [orgn]"</dev/null| \ 
esummary|xtract -pattern DocumentSummary -element Id>$whole
done

Then run this to obtain the sequences:

awk {'print $1,$2,$8'} species_counts.md|while read line
do
genus=`awk {'print $1'} <<< $line`
species=`awk {'print $2'} <<< $line`
number=`awk {'print $3'} <<< $line`
whole="$genus-$species.txt"
echo $whole $number
python get_rand_protein.py protein_ids/$whole $number
done
"""


from sys import argv
import random
import subprocess

with open(argv[1], 'r') as file_in:
	protein_ids = [line.strip() for line in file_in]
	number_of_genes = int(argv[2])
	rand_genes = random.sample(protein_ids, number_of_genes)
	for gene in rand_genes:
		seq = subprocess.check_output(['efetch', '-db', 'protein', '-id', '{}'.format(gene), '-format', 'fasta'])
		with open('random_sequences3.fas', 'a') as file_out:
			file_out.write(seq)
