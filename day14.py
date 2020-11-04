from hashlib import md5
from itertools import count
from collections import deque

salt = 'abc'
salt = 'ahsbgdzn'


def stretch(x, loop):
    x = md5(x.encode()).hexdigest()
    while loop > 0:
        x = md5(x.encode()).hexdigest()
        loop -= 1
    return x

def solve(loop=0):

	threes = deque()
	fives = deque()
	code = []

	for s in count(1):
		x = stretch(salt+str(s),loop)

		for c in range(len(x)-2):
			if c+4<len(x) and all([x[c]==x[c+n] for n in range(1,5)]):
				#print('found 5',x[c],' at',s,x)
				if (x[c],s) not in fives:
					fives.append((x[c],s))
			if all([x[c]==x[c+n] for n in range(1,3)]):
				#print('found 3',x[c],' at',s,)
				if ((x[c],s)) not in threes:
					threes.append((x[c],s))
					break

		if s > 27000:
			break

	# print(s)
	# print('3s',len(threes))
	# print('5s',len(fives))

	code = []
	for c, s in threes:
		for f, s2 in fives:
			if c==f and s2>s and s2-s<1000:
				code.append((c,s))
				break

	return code[63][1]


print('#1',solve())
print('#2',solve(2016))