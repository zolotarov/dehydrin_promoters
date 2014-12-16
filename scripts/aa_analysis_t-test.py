from scipy import stats
import numpy as np

"""
in aa_analysis_*.tsv:
1 - iupred
2 - aromaticity
3 - aliphatic index
4 - gravy
"""

parameter =4 

with open('aa_analysis_dehydrin.tsv', 'r') as deh_file:
	dehydrin_scores = [float(line.split('\t')[parameter]) for line in deh_file]

with open('aa_analysis_random.tsv', 'r') as rand_file:
	random_scores = [float(line.split('\t')[parameter]) for line in rand_file] 

# test for normality, result - data not normal, use levene test to test for homogeneity
# of varinces
print stats.shapiro(dehydrin_scores)


# The Levene test tests the null hypothesis that all input samples are 
# from populations with equal variances. Levene's test is an alternative
# to Bartlett's test in the case where there are significant 
# deviations from normality.
print stats.levene(dehydrin_scores, random_scores) # not homogeneous
# print stats.bartlett(dehydrin_scores, random_scores)

# return the mean and the standard error
print np.mean(dehydrin_scores), stats.sem(dehydrin_scores)
print np.mean(random_scores), stats.sem(random_scores)

# data not homogeneous
print stats.ttest_ind(dehydrin_scores, random_scores, equal_var = False)
