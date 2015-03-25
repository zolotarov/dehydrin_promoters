import cPickle
from collections import Counter

all_deh_d = cPickle.load(open("../results/all_deh_matches.pkl", "r"))

for val in all_deh_d:
	counter = 0
	empty_counter = 0
	for item in all_deh_d[val]:
		if 'Dehydrin' in item:
			counter += 1
		elif item == '':
			empty_counter += 1
	if (len(all_deh_d[val]) - counter - empty_counter) >= counter:
		print val, counter, empty_counter 

# for val in all_deh_d:
# 	print val, Counter(all_deh_d[val]).most_common(2)#[0]

# print all_deh_d['Ca_20934']
