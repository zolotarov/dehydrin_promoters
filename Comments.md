### Command used to count the number of unique dehydrins in Phytozome v9.0 release:
	 grep ">" scripts/dehydrins.fas|sed 's/|/ /g'|awk {'print $1'}| sort|uniq|wc -l

the total number of unique genes is 251 and the number of unique transcripts is 281 

**Aquca_038_00119** has 4 different transcripts and has a dehydrin and *reticulon* domain, the dehydrin domain is 7-39.

The K-segments: 
>Aquca_038_00119|Aquca_038_00119.1
HSESLMEKIKEKIHG

