from collections import deque


def part1(goal):

	elfs = deque([n for n in range(1,goal,2)])

	while len(elfs) > 1:
		#print(elfs)
		elfs.rotate(-2)
		elfs.pop()
		
	print('#1',elfs[0])


class Elf(object):
	"""docstring for Elf"""
	def __init__(self, idx):
		super(Elf, self).__init__()
		self.id = idx
		self.left = None
		self.right = None

	def eject(self):
		self.right.left = self.left
		self.left.right = self.right


def solve(n):
	ring = list(map(Elf,range(1,n+1)))
	for x in range(n):
		ring[x].left = ring[(x-1)%n]
		ring[x].right = ring[(x+1)%n]

	winner = ring[0]
	loser = ring[n//2]

	for x in range(n):
		#print(winner.id,'steals from',loser.id)
		loser.eject()
		loser = loser.right
		if (n-x)%2==1:
			loser = loser.right
		winner = winner.right
	return winner.id




def part2fail():
	elfs = deque([n for n in range(1,32100//3+1)])
	while len(elfs) > 1:
		#print(elfs)
		target = len(elfs)//2
		#print('target',elfs[target])
		#elfs[0][1]+= elfs[target][1]
		elfs.rotate(-target-1)
		elfs.pop()
		#print('pop',elfs.pop())
		elfs.rotate(target-1)
	print('#2-',elfs[0], elfs[0]*3)



def part1math(goal):
	c = 1
	while 2**c < goal:
		c+=1
	c-=1
	l = goal-2**c

	#print(2*l+1) 
	return 2*l+1

def part2math(goal):
	c = 1
	while 3**c < goal:
		c+=1
	c-=1
	l = goal - 3**c
	adj = 0
	if l-3**c > 0:
		adj = l-3**c
	#print(l+adj)
	return l+adj 


goal = 3012210


def part2():
	#print('#2',solve(goal))
	print('#2',part2math(goal),'(math)')


#part1(goal)
print('#1',part1math(goal),'(math)')
part2()
#part2b()
# 25: prune 13, 15,16, 18,19, 21,22, 24,25, 2,3, 5,6, 8,9, 11,12
# 25: 1,4,7,10,

#print('5',solve(5))

# for x in range(1,101):
# 	part2math(x)


# for x in range(240,250):
# 	print(x,solve(x))

# 12: 3,6,9,12
# 30: 3,6,9,12,15,18,21,24,27,30