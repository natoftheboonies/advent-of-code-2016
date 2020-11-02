
with open ('input3') as fp:
	input = [list(map(int,x.strip().split())) for x in fp.readlines()]

count = 0
for sides in input:
	sides = sorted(sides)
	if sides[0]+sides[1] > sides[2]:
		count += 1

print('#1',count)

count = 0
for i in range(0,len(input),3):
	# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
	box = list(zip(*input[i:i+3]))
	for x in box:
		sides = sorted(x)
		if sides[0]+sides[1] > sides[2]:
			count += 1

print('#2',count) # 1836
