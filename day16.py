

def grow(a):
	b = reversed(str(a))
	#b.reverse()
	b = ''.join(['0' if c == '1' else '1' for c in b ])
	ai = int(a,2)
	result = a+'0'+b
	return result


def checksum(a):
	result = ''
	for c in range(0,len(a),2):
		if a[c]==a[c+1]:
			result += '1'
		else:
			result += '0'
	if len(result)%2==1:
		return result
	else:
		return checksum(result)

def solve(a,size):
	while len(a)<size:
		a = grow(a)
	return checksum(a[:size])


def sample():
	assert grow('1')=='100'
	assert grow('0')=='001'
	assert grow('11111')=='11111000000'
	assert grow('111100001010')=='1111000010100101011110000'

	assert checksum('110010110100')=='100'
	assert solve('10000',20)=='01100'

a = '10111011111001111'

def part1():
	size = 272
	print('#1',solve(a,size))

def part2():
	size = 35651584
	print('#2',solve(a,size))

if __name__ == '__main__':
	sample()
	part1()
	part2()