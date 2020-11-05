from hashlib import md5
from collections import deque

maze_in = '''#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |V
####### x
'''.splitlines()

maze = {}
for y, row in enumerate(maze_in):
	for x, c in enumerate(row):
		maze[(x,y)]=c
		if c == 'S':
			start = (x,y)
		if c == 'V':
			goal = (x,y)

#just use 4x4 grid
start = (0,0)
goal = (3,3)

#print(start,goal)


U = (0,-1,'U')
D = (0,1,'D')
L = (-1,0,'L')
R = (1,0,'R')


code = 'pslxynzg'


whichdoor = 'UDLR'

def moves(path,pos):
	doors = md5((code+path).encode()).hexdigest()[:4]
	#print(path,doors)

	x,y = pos
	m = []
	for dx,dy,dd in U,D,L,R:
		if doors[whichdoor.index(dd)].isnumeric() or doors[whichdoor.index(dd)]=='a':
			#print(dd,'locked')
			continue
		nx = x+dx
		ny = y+dy
		if not (0 <= nx < 4 and 0 <= ny < 4):
			continue
		m.append(((nx,ny),dd))
	return m

def bfs(start, goal):
	queue = deque()
	queue.append(('',start))
	while queue:
		path, pos = queue.popleft()
		#visited.add(pos)
		for npos,dd in moves(path,pos):
			if npos in queue:
				continue
			if npos==goal:
				print('#1',path+dd)
				return path+dd
			queue.append((path+dd,npos))
		#break
	print('no path found')

def dfs(start, goal):
	paths = set()
	visited = set()
	queue = deque()
	queue.append(('',start))
	maxlen=0
	while queue:
		path, pos = queue.pop()
		#visited.add(pos)
		for npos,dd in moves(path,pos):
			if npos in queue:
				continue
			if npos==goal:
				if len(path+dd) > maxlen:
					maxlen = len(path+dd)
				continue
			queue.append((path+dd,npos))
		#break
	print('#2',maxlen)


bfs(start,goal)
dfs(start,goal)