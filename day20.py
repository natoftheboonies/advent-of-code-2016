input = '''5-8
0-2
4-7'''.splitlines()

with open('input20') as fp:
	input = fp.readlines()

ranges = []
for x in input:
	iprange = tuple(map(int,x.strip().split('-')))
	ranges.append(iprange)

candidate = min([ip[1] for ip in ranges])+1

relevant = [ip for ip in ranges if (ip[0] <= candidate and candidate <= ip[1])]
while relevant:
	#print(candidate, relevant)
	candidate = max([ip[1] for ip in relevant])+1
	relevant = [ip for ip in ranges if (ip[0] <= candidate and candidate <= ip[1])]

print('#1',candidate)

candidates = [ip[1]+1 for ip in ranges]

valid = []
for candidate in candidates:
	if candidate >= 2**32:
		continue
	for ip in ranges:
		if ip[0] <= candidate and candidate <= ip[1]:
			break
	else:
		valid.append(candidate)
print('#2',len(valid))
