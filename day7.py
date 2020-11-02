import re

good = re.compile(r'(?:^|\])(\w+)(?:\[|$)')
bad = re.compile(r'\[(\w+)\]')

def check(addr):
	supports_TLS = False
	for group in good.findall(addr):
		for c in range(len(group)-3):
			sub = group[c:c+4]
			if sub[0]==sub[3] and sub[1]==sub[2] and sub[0]!=sub[1]:
				supports_TLS = True
				#print(sub,'supports TLS')
				break
	for group in bad.findall(addr):
		for c in range(len(group)-3):
			sub = group[c:c+4]
			if sub[0]==sub[3] and sub[1]==sub[2] and sub[0]!=sub[1]:
				supports_TLS = False
				#print(sub,'does not support TLS')
				break
	return supports_TLS

assert check('abba[mnop]qrst')
assert not check('abcd[bddb]xyyx')
assert not check('aaaa[qwer]tyui')
assert check('ioxxoj[asdfgh]zxcvbn')

with open('input7') as fp:
	print('#1',sum([1 if check(line.strip()) else 0 for line in fp.readlines()]))


def check2(addr):
	supports_SSL = False
	accessors = set()
	blocks = set()
	for group in good.findall(addr):
		for c in range(len(group)-2):
			sub = group[c:c+3]
			if sub[0] == sub[2] and sub[0] != sub[1]:
				accessors.add(sub)
	for group in bad.findall(addr):
		for c in range(len(group)-2):
			sub = group[c:c+3]
			if sub[0] == sub[2] and sub[0] != sub[1]:
				blocks.add(sub)
	for acc in accessors:
		block = acc[1]+acc[0]+acc[1]
		if block in blocks:
			supports_SSL = True
	#print(accessors, blocks)
	return supports_SSL

assert check2('aba[bab]xyz')
assert not check2('xyx[xyx]xyx')
assert check2('aaa[kek]eke')
assert check2('zazbz[bzb]cdb')

with open('input7') as fp:
	print('#2',sum([1 if check2(line.strip()) else 0 for line in fp.readlines()]))
