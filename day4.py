
def checks(input):
	input = input.split('[')
	left, checksum = input[0],input[1][:-1]
	parts = left.split('-')
	sector = int(parts[-1])
	string = ''.join(parts[:-1])

	cnt = {}
	for x in string:
		if x.isalpha():
			cnt[x] = cnt.get(x,0)+1
	freq = [k for k, v in sorted(cnt.items(), key=lambda item: (-item[1],item[0]))]
	if ''.join(freq[:5])==checksum:
		return sector
	else:
		return 0

samples = '''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]'''.splitlines()

with open('input4') as fp:
	samples = [line.strip() for line in fp.readlines()]


print('#1',sum([checks(x) for x in samples]))

# https://stackoverflow.com/questions/16060899/alphabet-range-in-python
# map(chr, range(97, 123))

sample2 = 'qzmt-zixmtkozy-ivhz-343'

def decode(input):
	input = input.split('[')
	left, checksum = input[0],input[1][:-1]
	words = left.split('-')
	sector = int(words[-1])
	rot = sector%26
	return ' '.join([''.join([chr((ord(c)-97+rot)%26+97) for c in x]) for x in words[:-1]]), sector

for x in samples:
	if checks(x)>0 and 'northpole' in decode(x)[0]:
		print(decode(x))
		print('#2',decode(x)[1])
