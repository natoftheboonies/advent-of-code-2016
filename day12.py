



def run(inst,reg = {'a':0, 'b':0, 'c':0, 'd':0}):

	def get(x):
		if x.isalpha():
			return reg[x]
		else:
			return int(x)

	ptr = 0
	while ptr < len(inst):
		i = inst[ptr]
		#print(i)
		if i[0]=='cpy':
			_, x, y = i
			reg[y] = get(x)
		elif i[0] == 'inc':
			_, x = i
			reg[x]+=1
		elif i[0] == 'dec':
			_, x = i
			reg[x]-=1
		elif i[0] == 'jnz':
			_, x, y = i
			if get(x) != 0:
				ptr += get(y)
				continue

		ptr+=1

	return reg


sample = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
""".splitlines()

def runsample():
	inst = [s.split() for s in sample]
	reg = run(inst)
	print('#sample',reg['a'])

with open('input12') as fp:
	inst = [s.strip().split() for s in fp.readlines()]

def part1():
	reg = run(inst)
	print('#1',reg['a'])

def part2():
	reg = run(inst,{'a':0, 'b':0, 'c':1, 'd':0})
	print('#1',reg['a'])


if __name__ == '__main__':
	part1()
	part2()


