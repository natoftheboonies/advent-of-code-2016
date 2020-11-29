
fav = 1350

def eval(x,y):
	c = x*x + 3*x + 2*x*y + y + y*y + fav
	return bin(c).count('1')%2

from collections import deque

def moves(pos):
	x,y = pos
	for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
		nx = x+dx
		ny = y+dy
		if nx < 0 or ny < 0 or eval(nx,ny) == 1:
			continue
		yield (nx,ny)

def bfs(start, goal):
	assert eval(*goal)==0
	dist = dict()
	visited = set()
	queue = deque()
	queue.append((0,start))
	while queue:
		dist, pos = queue.popleft()
		visited.add(pos)
		for npos in moves(pos):
			if npos in visited or npos in queue:
				continue
			if npos==goal:
				print('#1',dist+1)
				return dist+1
			queue.append((dist+1,npos))
	print('no path found')

def bfs2(start, maxdist):
	dist = dict()
	visited = set()
	queue = deque()
	queue.append((0,start))

	while queue:
		dist, pos = queue.popleft()
		if dist > maxdist:
			continue
		visited.add(pos)
		for npos in moves(pos):
			if npos in visited or npos in queue:
				continue
			if npos==goal:
				print('#1',dist+1)
				return dist+1
			queue.append((dist+1,npos))
	print('#2',len(visited))

start = (1,1)
goal = (31,39)
bfs(start,goal)
bfs2(start,50)
