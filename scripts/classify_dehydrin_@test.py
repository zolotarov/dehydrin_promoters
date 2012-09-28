from Bio import AlignIO, Motif, SeqIO
from Bio.Alphabet import IUPAC

import re

class PWM(object):
	def __init__(self, alignment_file):
		self.file = alignment_file
		self.alphabet = IUPAC.protein

	def pwm_maker(self):
		alignment_file = self.file
		alignment = AlignIO.read(alignment_file, "fasta", alphabet=self.alphabet)
		m = Motif.Motif(self.alphabet)
		for a in alignment:
			m.add_instance(a.seq)
		return m


class Dehydrin(object):
	def __init__(self, sequence):

		self.sequence = sequence


k_segs = PWM("../sequences/k-segs.fas").pwm_maker()
# k_m = k_segs.pwm_maker()
print k_segs.format("transfac")

sequence = """
MSGYPIQSTDEHGNLVPQRDEYGNLVHQTGTGHTGTGQTGPGTGHTGTGGYGGHTGTGGY
GAGDGTGTGQHTGTGLGTGTGQHAGTGLGTGAGHHTGTGVGGEQHGGVLRRSGSSSSSSS
SEDDGMGGRRKKGLKQKIKEKLPGGQKETQPGYGAGTTGAGTTGPGYGTTTGAGAGYGTT
EQPHEKKGMIEKIKEKLPGHHA"""

deh_sequence = Dehydrin(sequence.replace('\n','').strip())

print deh_sequence.sequence