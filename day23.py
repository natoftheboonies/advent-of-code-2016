
def run(inst,reg = {'a':0, 'b':0, 'c':0, 'd':0}):

	def get(x):
		if x.isalpha():
			return reg[x]
		else:
			return int(x)

	ptr = 0
	count = 0
	while ptr < len(inst):
		count+=1	
		i = inst[ptr]
		#print(ptr,i)
		if ptr == 4: # optimization
			reg['a'] += reg['b']*reg['d']
			reg['c'] = 0
			reg['d'] = 0
			ptr = 10
			continue
		if i[0]=='cpy':
			_, x, y = i
			if y in reg:
				reg[y] = get(x)
			else:
				print('invalid cpy target',i)
				print(reg)
		elif i[0]=='tgl':
			_, x = i
			x = get(x)
			if ptr+x < len(inst):
				tog_i = inst[ptr+x]
				if len(tog_i)==2:
					if tog_i[0]=='inc':
						tog_i[0] = 'dec'
					else:
						tog_i[0] = 'inc'
				elif len(tog_i)==3:
					if tog_i[0]=='jnz':
						tog_i[0]='cpy'
					else:
						tog_i[0]='jnz'
			else:
				#print('no toggle inst',ptr+x)			
				pass
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
				#print('jump to',ptr)
				continue

		ptr+=1

	#print(count)
	return reg


sample = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
""".splitlines()

def runsample():
	inst = [s.split() for s in sample]
	reg = run(inst)
	print('#sample',reg['a'])


def part1():
	with open('input23') as fp:
		inst = [s.strip().split() for s in fp.readlines()]
	reg = run(inst,{'a':7, 'b':0, 'c':0, 'd':0})
	print('#1',reg['a']) #10890

def part2():
	with open('input23') as fp:
		inst = [s.strip().split() for s in fp.readlines()]
	reg = run(inst,{'a':12, 'b':0, 'c':0, 'd':0})
	print('#2',reg['a']) # 479007450


if __name__ == '__main__':
	#runsample()
	part1()
	part2()


