def disks_from_lines(lines):
    disks = {}
    for line in lines:
        data = line.strip().split()
        pos = tuple(map(int, [c[1:] for c in data[0].split("-")[1:]]))
        size = int(data[1][:-1])
        used = int(data[2][:-1])
        avail = int(data[3][:-1])
        assert data[1][-1] == "T"
        assert data[2][-1] == "T"
        assert data[3][-1] == "T"
        assert avail == size - used
        # print(pos, size, used, avail)
        disks[pos] = (size, used, avail)
    return disks


def real_lines():
    with open("input22") as fp:
        fp.readline()  # cmd
        fp.readline()  # header
        return fp.readlines()


def sample_lines():
    sample = """Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""".splitlines()
    return sample[1:]


def part1():
    lines = real_lines()
    # lines = sample_lines()
    disks = disks_from_lines(lines)

    count = 0
    possible = {}
    for a in disks:
        if disks[a][1] == 0:
            continue
        possible[a] = []
        for b in disks:
            if a == b or disks[a][1] > disks[b][2]:
                continue
            else:
                count += 1
                possible[a].append(b)
    print("#1", count)
    # for a in possible:
    # 	if not possible[a]:
    # 		print(a)


def part2sample():
    lines = sample_lines()
    disks = disks_from_lines(lines)
    pos = max([disk for disk in disks if disk[1] == 0])
    goal = (0, 0)
    print(pos, "->", goal)
    # bfs (prob A* soon) to move data.
    empty = [disk for disk in disks if disks[disk][1] == 0]
    print(empty)
    # move empty to space between pos and goal (target) which is adjacent to pos that has free-space for pos.
    # repeat until goal.


def part2():
    lines = real_lines()
    disks = disks_from_lines(lines)
    pos = max([disk for disk in disks if disk[1] == 0])  # (35, 0)
    goal = (0, 0)
    # print(pos, '->', goal)
    # bfs (prob A* soon) to move data.
    empty = [disk for disk in disks if disks[disk][1] == 0][0]
    # print('empty',empty) #35,27

    # x2+,y17 are full (walls)
    # goal .... pos
    # 01###########
    # ............_
    # so first, gotta move empty around the wall
    # wall at 1,17.
    gap = (1, 17)
    dist = abs(empty[0] - gap[0]) + abs(empty[1] - gap[1])
    # print(dist)
    # then go from 1,17 to goal, 35,0
    dist += abs(pos[0] - gap[0]) + abs(pos[1] - gap[1])
    # print(dist)
    # now:
    # ...34.....G_
    # ............
    # so each move down,left,left,up,right x34
    # G_.......
    print("#2", dist + (pos[0] - 1) * 5)

    # 263 too low
    # 268 wrong, 270 wrong
    # 273 too high


if __name__ == "__main__":
    part1()
    # part2sample()
    part2()
