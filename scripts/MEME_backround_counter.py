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
