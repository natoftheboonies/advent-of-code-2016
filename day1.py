# 2016 day 1 with complex numbers. :)

path = "R2, L3"
input2 = "R2, R2, R2"
input3 = "R5, L5, R5, R3"

with open('input1') as fp:
	solve = fp.read().strip()
#solve = 'R8, R4, R4, R8'
steps = solve.split(', ')

pos = 0
d = -1j

for step in steps:
	d *= -1j if step[0] == 'R' else 1j
	pos += d*int(step[1:])

print('#1',int(abs(pos.real)+abs(pos.imag)))

pos = 0
d = -1j

visited = set([pos])
for step in steps:
	d *= -1j if step[0] == 'R' else 1j
	for _ in range(int(step[1:])):
		pos += d
		if pos in visited:
			break
		visited.add(pos)
	else:
		continue
	break


print('#2',int(abs(pos.real)+abs(pos.imag)))
