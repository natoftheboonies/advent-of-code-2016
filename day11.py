from itertools import combinations

sample = '''F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM '''.splitlines()

# generator +, chip -
def checkfloor(floor):
	if not floor or floor[-1]<0:
		# no generators
		return True
	# no chip without it's generator
	return all(-chip in floor for chip in floor if chip < 0)


def move(state):
	"""hey, this is the find neighbors"""
	moves = []
	e, floors = state[0], state[1:]
	for e_new in [e+1, e-1]:
		if e_new > 3 or e_new < 0:
			continue
		if e_new==0 and len(floors[0])==0:
			continue
		if e_new==1 and e==2 and len(floors[0])==0 and len(floors[1])==0:
			continue
		tried_pair = False
		for choice in list(combinations(floors[e],2))+list(combinations(floors[e],1)):

			if len(choice)==2 and e_new < e:
				# don't bring 2 things down
				pass
			if sum(choice)==0:
				# if moving chip+generator up, equivalent to any other pair
				if tried_pair:
					continue


			floors_new = list(floors[:min(e_new,e)])
			if e_new > e:
				floors_new.append(tuple(x for x in floors[e] if x not in choice))
				floors_new.append(tuple(sorted(floors[e_new]+choice)))
			else:
				floors_new.append(tuple(sorted(floors[e_new]+choice)))
				floors_new.append(tuple(x for x in floors[e] if x not in choice))
			ok = True
			for check in floors_new[-2:]:
				if not checkfloor(check):
					#print('invalid floor',x)
					ok = False
			if not ok:
				continue
			floors_new.extend(floors[max(e_new,e)+1:])
			assert len(floors_new)==4
			state_new = (e_new,*floors_new)
			if sum(choice)==0:
				tried_pair = True
			#print(choice, state_new)
			moves.append(state_new)
	return moves

from collections import deque

def cost(state):
	cost = 0
	for n, floor in enumerate(state[1:]):
		cost += len(floor)*(3-n)
	return cost

import heapq

def bfs(start):
	visited = set()
	moves = {start:0}
	queue = []
	heapq.heappush(queue,(0,start))
	#queue.append((start,0))

	iters=0
	while queue:
		iters+=1
		_,state = heapq.heappop(queue)
		depth = moves[state]
		visited.add(state)
		for next_state in move(state):
			if all(len(floor)==0 for floor in next_state[1:-1]):
				print('woohoo!',iters,next_state)
				return depth+1
			if next_state in visited:
				continue
			if next_state in moves and moves[next_state]<depth+1:
				continue
			moves[next_state] = depth+1
			heapq.heappush(queue,(depth-len(next_state[-1])*4,next_state))
			#queue.append((, depth+1))
	print('no goal reached')


# generator +, chip -
hydrogen, lithium = 1, 2

# elevator, floors0..3
state = (0,tuple(sorted((-hydrogen,-lithium))),tuple((hydrogen,)),tuple((lithium,)),())
print(state)
print('#sample',bfs(state))


# hardcoded input, gen < 0, microchip > 0
promethium, cobalt, curium, ruthenium, plutonium = 1, 2, 3, 4, 5
start = (0, tuple(sorted((promethium,-promethium))),
	tuple(sorted((cobalt, curium, ruthenium, plutonium))),
	tuple(sorted((-cobalt, -curium, -ruthenium, -plutonium))), ()
)

print(start)

print('#1',bfs(start))
# #1 33
# [Finished in 22.8s]

elerium, dilithium = 6, 7
start = (0, tuple(sorted((promethium,-promethium,elerium,-elerium,dilithium,-dilithium))),
	tuple(sorted((cobalt, curium, ruthenium, plutonium))),
	tuple(sorted((-cobalt, -curium, -ruthenium, -plutonium))), ()
)

#print('#2',bfs(start))
# #2 57
# [Finished in 3673.3s]