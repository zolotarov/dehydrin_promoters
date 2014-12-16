# Obtain protein IDs from NCBI

To get all protein IDs for species used in the analysis the following command was used (using NCBI Eutils):

```bash
awk {'print $1,$2'} species.md|while read line
do
genus=`awk {'print $1'} <<< $line`
species=`awk {'print $2'} <<< $line`
whole="$genus-$species.txt"
esearch -db protein -query "$genus $species [orgn]"</dev/null| \ 
esummary|xtract -pattern DocumentSummary -element Id>$whole
done
```

The "`< /dev/null`" input redirection construct prevents esearch from "draining" the remaining lines from stdin. Otherwise only first line is considered
