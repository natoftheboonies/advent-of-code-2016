
def scramble(start, lines):
	result = list(start)
	for line in lines:
		inst = line.strip().split()
		if inst[0]=='swap':
			if inst[1]=='position':
				a = int(inst[2])
				b = int(inst[5])
			elif inst[1]=='letter':
				a = result.index(inst[2])
				b = result.index(inst[5])
			else:
				print('unknown swap:',line)
			tmp = result[a]
			result[a] = result[b]
			result[b] = tmp
		elif inst[0] == 'reverse':
			a = int(inst[2])
			b = int(inst[4])
			result = result[:a]+list(reversed(result[a:b+1]))+result[b+1:]
		elif inst[0] == 'move':
			a = int(inst[2])
			b = int(inst[5])
			tmp = result.pop(a)
			result.insert(b,tmp)
		elif inst[0] == 'rotate':
			if inst[1] == 'based':
				a = result.index(inst[6])
				if a >= 4:
					a += 1
				for _ in range(a+1):
					result.insert(0,result.pop())
			elif inst[1]=='left':
				a = int(inst[2])
				for _ in range(a):
					result.append(result.pop(0))
			elif inst[1]=='right':
				a = int(inst[2])
				for _ in range(a):
					result.insert(0,result.pop())
			else:
				print('unknown rotate:',line)
		else:
			print('unknown:',line)
		#print('after',line,'result:',''.join(result))
	return ''.join(result)


def sample():
	lines = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
""".splitlines()
	start = 'abcde'
	assert scramble(start,lines)=='decab'

with open('input21') as fp:
	lines = fp.readlines()

def part1():
	start = 'abcdefgh'
	print('#1',scramble(start,lines))

from itertools import permutations
def part2():
	# brute force ;)
	scrambled = 'fbgdceah'
	for test in permutations(scrambled):
		if scramble(''.join(test),lines)==scrambled:
			print('#2',''.join(test))
			break

if __name__ == '__main__':
	sample()
	part1()
	part2()