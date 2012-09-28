import re
from sys import exit

class FindMotif(object):
	"""docstring for Sequence"""
	def __init__(self, sequence):
		self.sequence = sequence
		self.regex = None

		nucleotides = ['A', 'C', 'T', 'G']
		
		for letter in self.sequence:
			if letter not in nucleotides:
				print "The provided sequence is not a proper DNA sequence"
				exit(0)
			else:
				continue

	def find_motif(self, regex):
		self.sequence = self.sequence
		self.regex = regex

		results = [hit.start() for hit in re.finditer(self.regex, self.sequence)]
		return results

	def reverse_complement(self):

		complement_dic = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
		self.sequence = self.sequence

		"""
		reverse complementation can be done in one step:
		# rev_comp = ''.join([complement_dic[self.sequence[i]] for i in range(-1, -(len(self.sequence) + 1), -1)])

		rev_comp = ''.join([complement_dic[self.sequence[i]] for i in range(-1, -(len(self.sequence) + 1), -1)])
		or in three steps using a built-in list.reverse() method.

		The built-in method is marginally faster (3 ms for a very large sequence)
		"""


		seq_list = list(self.sequence)
		seq_list.reverse()
		rev_comp = ''.join([complement_dic[i] for i in seq_list])
		
		rev_comp_seq = FindMotif(rev_comp)
		return rev_comp_seq

seq = """ATGATGATGTTACCAGAAGCATGCATAGCCAACATCCTTGCCTTCACATCTCCGGCGGAT
GCATTCTCGTCGTCAGAGGTCTCTTCGGTTTTCCGGTTAGCCGGAGACTCTGATTTCGTA
TGGGAAAAGTTTCTACCATCGGATTACAAAAGCCTCATCTCTCAATCTACTGATCATCAT
TGGAATATTTCTTCCAAAAAAGAAATTTATCGATGTTTATGTGACTCTCTTCTCATCGAT
AATGCTCGAAAGCTGTTCA""".replace('\n','').strip()

sequ = FindMotif(seq)

sequ.reverse_complement().sequence
