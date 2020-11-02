sample = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".splitlines()

with open('input6') as fp:
	sample = fp.readlines()

inputs = [list(x.strip()) for x in sample]

print("#1 ",end='')
for b in zip(*inputs):
	print(max(set(b), key=b.count),end='')
print()
print("#2 ",end='')
for b in zip(*inputs):
	print(min(set(b), key=b.count),end='')
print()

