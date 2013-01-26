#===================================================================

# Reference filename: motif-00000.stdout
#
source("/home/yzolotarov/gimsan_cmdline/bin/conf_pval_only.R")
library(MASS)

sample<-scan("/home/yzolotarov/gimsan_cmdline/20121121_KS_dehydrins_promoters_dicots.fas/statsig/scores.width008")
getConfPvalLat(13.82, sample, conf=0.1, mins=7, maxs=200)
