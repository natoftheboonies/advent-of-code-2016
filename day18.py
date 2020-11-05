row1 = '..^^.'

def nextrow(row):
	nextrow = ''
	for n in range(len(row)):
		l = False if n == 0 or row[n-1] == '.' else True
		c = False if row[n] == '.' else True
		r = False if n == len(row)-1 or row[n+1] == '.' else True
		if (c and ((l and not r) or (not l and r))) or (not c and ((l and not r) or (not l and r))):
			nextrow += '^'
		else:
			nextrow += '.'
	return nextrow

assert nextrow(row1) == '.^^^^'
assert nextrow(nextrow(row1)) == '^^..^'

def sample():
	row = '.^^.^.^^^^'
	count = 0
	for _ in range(10):
		count += row.count('.')
		row = nextrow(row)
	return count

def part1():
	with open('input18','r') as fp:
		row = fp.readline().strip()
	count = 0
	for _ in range(40):
		count += row.count('.')
		row = nextrow(row)
	return count

def part2():
	with open('input18','r') as fp:
		row = fp.readline().strip()
	# seen = set()
	count = 0
	for c in range(400000):
		count += row.count('.')
		row = nextrow(row)
		# if row in seen:
		# 	print('repeat at',c)
		# seen.add(row)
	return count

if __name__ == '__main__':
	assert sample()==38
	print('#1',part1())
	print('#2',part2())

