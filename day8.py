

def show(grid):
	for row in grid:
		print(''.join(['#' if col == 1 else ' ' for col in row]))
	print()

def rect(grid, a, b):
	for y in range(b):
		for x in range(a):
			grid[y][x]=1


def rotcol(grid, a, n):
	col = [y[a] for y in grid]
	for t in range(n):
		col.insert(0,col.pop())
	for y in range(len(grid)):
		grid[y][a] = col[y]

def rotrow(grid, b, n):
	for t in range(n):
		grid[b].insert(0,grid[b].pop())


def run(grid, commands):
	for inst in commands:
		cmd = inst.strip().split()
		if cmd[0]=='rect':
			a,b = map(int,cmd[1].split('x'))
			rect(grid,a,b)
		elif cmd[0] == 'rotate' and cmd[1] == 'column':
			a = int(cmd[2].split('=')[1])
			n = int(cmd[4])
			rotcol(grid,a,n)
		elif cmd[0] == 'rotate' and cmd[1] == 'row':
			b = int(cmd[2].split('=')[1])
			n = int(cmd[4])
			rotrow(grid,b,n)
	count = sum([sum(y) for y in grid])
	print('#1',count)

	show(grid) # AFBUPZBJPS

def sample():

	grid = [[0]*7 for _ in range(3)]

	commands = '''rect 3x2
	rotate column x=1 by 1
	rotate row y=0 by 4
	rotate column x=1 by 1'''.splitlines()

	run(grid,commands)

def solve():

	grid = [[0]*50 for _ in range(6)]
	with open('input8') as fp:
		commands = fp.readlines()

	run(grid,commands)

if __name__ == '__main__':
	#sample()
	solve()
