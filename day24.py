from collections import deque


def bfs(maze, goals, part2=False):

    dist = dict()
    visited = set()  # (pos, keys)
    queue = deque()
    # dist, pos, keys met
    queue.append((0, goals["0"], ("0")))

    def moves(pos):
        x, y = pos
        #m = []
        for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or maze[(nx, ny)] == "#":
                continue
            yield (nx, ny)
            #m.append((nx, ny))
        #return m

    while queue:
        dist, pos, keys = queue.popleft()
        visited.add((pos, keys))
        for npos in moves(pos):
            nkeys = keys
            if maze[npos].isnumeric() and maze[npos] not in keys:
                nkeys = tuple(sorted(list(keys) + [maze[npos]]))
            if (npos, nkeys) in visited or (dist + 1, npos, nkeys) in queue:
                continue
            if nkeys == tuple(sorted(goals.keys())) and (not part2 or npos == goals["0"]):
                # print('#1',dist+1)
                return dist + 1
            if maze[npos].isnumeric() and maze[npos] not in keys:
                queue.append((dist + 1, npos, nkeys))
            else:
                queue.append((dist + 1, npos, nkeys))
    print("no path found")


def parselines(lines):
    maze = {}
    goals = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            maze[(x, y)] = char
            if char.isnumeric():
                goals[char] = (x, y)
    return maze, goals


def sample():
    lines = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########
""".splitlines()
    maze, goals = parselines(lines)

    print("start", goals["0"])

    print("#sample", bfs(maze, goals))


def part1():
    with open("input24") as fp:
        lines = fp.readlines()
    maze, goals = parselines(lines)

    # print('start',goals['0'])

    part1 = bfs(maze, goals)
    print("#1", part1)  # 464


def part2():
    with open("input24") as fp:
        lines = fp.readlines()
    maze, goals = parselines(lines)

    part2 = bfs(maze, goals, True)
    print("#2", part2)  # 652
    # not 664, somebody else's answer.


if __name__ == "__main__":
    # sample()
    part1()
    part2()
