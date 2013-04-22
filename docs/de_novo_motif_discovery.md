# *de novo* motif analysis
## BioProspector
* **Concatenate monocot and dicot sequences:**

```bash
cat sorbi_prom_1K.fas zeama_prom_1K.fas setit_prom_1K.fas panvi_prom_1K.fas orysa_prom_1K.fas bradi_prom_1K.fas > monocots.fas

cat aquco_prom_1K.fas araly_prom_1K.fas arath_prom_1K.fas brara_prom_1K.fas capru_prom_1K.fas carpa_prom_1K.fas citcl_prom_1K.fas citsi_prom_1K.fas cucsa_prom_1K.fas eucgr_prom_1K.fas frave_prom_1K.fas glyma_prom_1K.fas gosra_prom_1K.fas linus_prom_1K.fas maldo_prom_1K.fas manes_prom_1K.fas medtr_prom_1K.fas mimgu_prom_1K.fas phavu_prom_1K.fas phypa_prom_1K.fas poptr_prom_1K.fas prupe_prom_1K.fas ricco_prom_1K.fas solly_prom_1K.fas soltu_prom_1K.fas theca_prom_1K.fas theca_prom_1K.fas theha_prom_1K.fas vitvi_prom_1K.fas > dicots.fas
```

* **Re-format multiline FASTA to single-line accepted by BioProspector**

`FASTA_multi_to_oneline.py` script:

```python
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from sys import argv
import random


out_filename = str(argv[1]).split('.')[0] + "_oneline.fas"

with open(out_filename, "w") as out_file:
        for record in SeqIO.parse(argv[1], "fasta"):
                rec_id = ">" + str(record.id).split('|')[0] + "\n"
                seq = str(record.seq) + "\n"
                if "Sequenceunavailable" in record.seq:
                        continue
                elif "R" in seq:
                    seq = seq.replace('R', random.choice('AG'))
                elif "Y" in seq:
                    seq = seq.replace('Y', random.choice('CT'))
                elif "S" in seq:
                    seq = seq.replace('S', random.choice('GC'))
                elif "W" in seq:
                    seq = seq.replace('W', random.choice('AT'))
                elif "K" in seq:
                    seq = seq.replace('K', random.choice('GT')) 
                elif "M" in seq:
                    seq = seq.replace('M', random.choice('AC'))
                elif "B" in seq:
                    seq = seq.replace('B', random.choice('CGT'))
                elif "D" in seq:
                    seq = seq.replace('D', random.choice('AGT'))
                elif "H" in seq:
                    seq = seq.replace('H', random.choice('ACT'))
                elif "V" in seq:
                    seq = seq.replace('V', random.choice('ACG'))
                else:
                        out_file.write(rec_id)
                        out_file.write(seq)
```
```bash
python FASTA_multi_to_oneline.py dicots.fas
```

* **Create background files**

In `/home/yzolotarov/BioProspector`:

```bash
./genomebg.linux -i ../sequences/promoters/monocots_oneline.fas -o monocots.bkg
```

* **Reformat promoter files to single line as above**

In `/home/yzolotarov/dehydrin_promoters/sequences/promoters/monocot`:

```bash
for file in *.fas; do python FASTA_multi_to_oneline.py $file; done
```
Repeat the same for dicot promoters

* **Run BioProspector for every promoter file:**

Returns 10 motif sequences of size 10

```bash
./BioProspector.linux -i /home/yzolotarov/dehydrin_promoters/sequences/promoters/monocot/KS_dehydrins_promoters_mono_oneline.fas -o KS_mono.bioprospector -f monocots.bkg -W 10 -r 10
```

* **Parse BioProspector results into MotifVoter format**

```python
"""
This script will parse the BioProspector results file into a MotifVoter
template
"""


from sys import argv

# second argument is the original promoter file
with open(argv[2], 'r') as promoter_file:
    names = [line.strip().split('>')[1] for line in promoter_file if ">" in line]

# print names

names_dict = dict((name, number) for number, name in enumerate(names))
# print names_dict

# first argument is the BioProspector results file
input_file = open(
    argv[1], 'r').read().replace('******************************', '')

for item in input_file.split('Motif #')[1:]:
    print ('\n' + "MOTIF FINDER: BioProspector")
    print "MOTIF:", item.split('>')[0].split("(")[1].split('/')[0]
    print "INSTANCES:"
    for part in item.split('>')[1:]:
        sequence_id = part.split('\t')[0]
        motif_sequence = part.split('\t')[3].split('\n')[1]
        direction = part.split('\t')[3].split('\n')[0].split(' ')[0]
        location = part.split('\t')[3].split('\n')[0].split(' ')[1]
        if direction == 'f':
            location_adjusted = -1000 + int(location) - 1
            direction_sign = '+'
        elif direction == 'r':
            location_adjusted = -int(location)
            direction_sign = '-'

        to_print = str(names_dict[sequence_id]) + ',' + str(
            location_adjusted) + ',' + motif_sequence + ',' + direction_sign
        print to_print
```

In `/home/yzolotarov/BioProspector`:

```bash
python bioprospector_parser.py SKn_mono.bioprospector ../dehydrin_promoters/sequences/promoters/monocot/SKn_dehydrins_promoters_mono_oneline.fas > SKn_mono.MotifVoter
```

## MEME

* **Create Markov background model**

This is basically the frequency of single nucleotides and di-nucleotides.  

In `/home/yzolotarov/sequences/promoters` run `python MEME_backround_counter.py monocots_oneline.fas > monocots.MEMEbkg`, repeat with `dicots_oneline.fas`

```python
from sys import argv

all_lines = ''
with open(argv[1], 'r') as input_file:
    for line in input_file:
        if ">" in line:
            continue
        else:
            all_lines += line.strip()

all_lines = all_lines.upper()
length = float(len(all_lines))


a = all_lines.count('A') 
c = all_lines.count('C')
g = all_lines.count('G')
t = all_lines.count('T')


aa = all_lines.count('AA')
ac = all_lines.count('AC')
ag = all_lines.count('AG')
at = all_lines.count('AT')
ca = all_lines.count('CA')
cc = all_lines.count('CC')
cg = all_lines.count('CG')
ct = all_lines.count('CT')
ga = all_lines.count('GA')
gc = all_lines.count('GC')
gg = all_lines.count('GG')
gt = all_lines.count('GT')
ta = all_lines.count('TA')
tc = all_lines.count('TC')
tg = all_lines.count('TG')
tt = all_lines.count('TT')

print ('A' + '\t' + "%0.3f" % (a/length))
print ('C' + '\t' + "%0.3f" % (c/length))
print ('G' + '\t' + "%0.3f" % (g/length))
print ('T' + '\t' + "%0.3f" % (t/length))

print ('AA' + '\t' + "%0.3f" % (aa/length))
print ('AC' + '\t' + "%0.3f" % (ac/length))
print ('AG' + '\t' + "%0.3f" % (ag/length))
print ('AT' + '\t' + "%0.3f" % (at/length))
print ('CA' + '\t' + "%0.3f" % (ca/length))
print ('CC' + '\t' + "%0.3f" % (cc/length))
print ('CG' + '\t' + "%0.3f" % (cg/length))
print ('CT' + '\t' + "%0.3f" % (ct/length))
print ('GA' + '\t' + "%0.3f" % (ga/length))
print ('GC' + '\t' + "%0.3f" % (gc/length))
print ('GG' + '\t' + "%0.3f" % (gg/length))
print ('GT' + '\t' + "%0.3f" % (gt/length))
print ('TA' + '\t' + "%0.3f" % (ta/length))
print ('TC' + '\t' + "%0.3f" % (tc/length))
print ('TG' + '\t' + "%0.3f" % (tg/length))
print ('TT' + '\t' + "%0.3f" % (tt/length))
```
* **Run MEME**

```bash
for file in *oneline.fas; do meme $file -text -dna -mod anr -nmotifs 10 -w 10 -revcomp -bfile ../../../results/MEME/dicots.MEMEbkg > $file.MEME; done
```
* **Parse MEME results into MotifVoter format**

```python
from sys import argv
import re

# second argument is the original promoter file
with open(argv[2], 'r') as promoter_file:
    names = [line.strip().split('>')[1] for line in promoter_file if ">" in line]
names_dict = dict((name[0:24], number) for number, name in enumerate(names))


input_file = open(argv[1], 'r').read()

for m in re.finditer('MOTIF.+\d{3}', input_file):
    motif_n = (m.group(0)).split('\t')[0]
    e_value = (m.group(0)).split('E-value = ')[-1]

    if float(e_value) <= 5e-2:
        motifs = input_file.split(motif_n)[1].split('sites sorted by position p-value')[1].split('--------------------------------------------------------------------------------')[1].split('\n')[3:]
        consensus = input_file.split(motif_n)[1].split('sites sorted by position p-value')[0].split('Multilevel')[1].split('\n')[0].strip()
        print ('\n' + "MOTIF FINDER: MEME")
        print "MOTIF:", consensus
        print "INSTANCES:"
        for motif in motifs:
            if motif:
                name = motif.split(' ')[0].split('|')[0]
                if name:
                    seq_number = names_dict[motif.split(' ')[0].split('|')[0]]
                
                direction = re.search("\s+[+|-]\s+", motif).group(0).strip()
                location = -(int(re.search("\s+\d+\s+", motif).group(0).strip())) if direction == '-' else (-1000 + int(re.search("\s+\d+\s+", motif).group(0).strip()) - 1)
                
                
                to_print = str(names_dict[name]) + ',' + str(
            location) + ',' + consensus + ',' + direction
                print to_print
```

In `/home/yzolotarov/dehydrin_promoters/results/MEME`

```bash
python MEME_parser.py YnSKn_di.MEME ../../sequences/promoters/dicot/YnSKn_dehydrins_promoters_di_oneline.fas > YnSKn_di.MEME.MotifVoter
```


## MDscan


```bash
./MDscan.linux -i ../dehydrin_promoters/sequences/promoters/KS_dehydrins_promoters_oneline.fas -w 10 -f ../BioProspector/all_used.bkg -r 10 -o KS.mdscan
```




## Programs that didn't work
*  GALF_P
Found TATA boxes and repeats, not usefult

* MoAn
Couldn't get it to compile