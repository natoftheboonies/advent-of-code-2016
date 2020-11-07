
def run(inst,reg = {'a':0, 'b':0, 'c':0, 'd':0}):

	def get(x):
		if x.isalpha():
			return reg[x]
		else:
			return int(x)
	emit = []
	ptr = 0
	while ptr < len(inst):
		i = inst[ptr]
		#print(i)
		if ptr == 2:
			reg['d'] += 362*reg['c']
			reg['b'] = 0
			reg['c'] = 0
			ptr = 8
			continue
		if i[0]=='cpy':
			_, x, y = i
			reg[y] = get(x)
		elif i[0]=='out':
			_, x = i
			emit.append(get(x))
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
		if len(emit)>10:
			#print(''.join(map(str,emit)))
			break
	return ''.join(map(str,emit))

with open('input25') as fp:
	inst = [s.strip().split() for s in fp.readlines()]

from itertools import count

def part1():
	for a in count(1):
		eg = run(inst,{'a':a, 'b':0, 'c':1, 'd':0})
		if eg[:10] == '0101010101' or eg[:10]=='1010101010':
			break
		# if a%100==0:
		# 	print(a)
	print('#1',a)

if __name__ == '__main__':
	part1()
