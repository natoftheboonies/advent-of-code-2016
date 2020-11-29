from collections import deque

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")

logging.debug("This is a log message.")


def part1(goal):

    elfs = deque([n for n in range(1, goal, 2)])

    while len(elfs) > 1:
        logging.debug(elfs)
        elfs.rotate(-2)
        elfs.pop()

    print("#1", elfs[0])


class Elf(object):
    """docstring for Elf"""

    def __init__(self, idx: int):
        super(Elf, self).__init__()
        self.id = idx
        self.left = None
        self.right = None

    def eject(self):
        self.right.left = self.left
        self.left.right = self.right


def solve(n: int):
    ring = list(map(Elf, range(1, n + 1)))
    for x in range(n):
        ring[x].left = ring[(x - 1) % n]
        ring[x].right = ring[(x + 1) % n]

    winner = ring[0]
    loser = ring[n // 2]

    for x in range(n):
        logging.debug(f"{winner.id} steals from {loser.id}")
        loser.eject()
        loser = loser.right
        if (n - x) % 2 == 1:
            loser = loser.right
        winner = winner.right
    return winner.id


def part1math(goal):
    c = 1
    while 2 ** c < goal:
        c += 1
    c -= 1
    l = goal - 2 ** c
    return 2 * l + 1


def part2math(goal):
    c = 1
    while 3 ** c < goal:
        c += 1
    c -= 1
    l = goal - 3 ** c
    adj = 0
    if l - 3 ** c > 0:
        adj = l - 3 ** c
    return l + adj


goal = 3012210


def part2():
    #print("#2", solve(goal))
    print('#2',part2math(goal),'(math)')


# part1(goal)
print("#1", part1math(goal), "(math)")
part2()
# part2b()
# 25: prune 13, 15,16, 18,19, 21,22, 24,25, 2,3, 5,6, 8,9, 11,12
# 25: 1,4,7,10,

# print('5',solve(5))

# for x in range(1,101):
#   part2math(x)

# for x in range(240,250):
#   print(x,solve(x))

# 12: 3,6,9,12
# 30: 3,6,9,12,15,18,21,24,27,30
