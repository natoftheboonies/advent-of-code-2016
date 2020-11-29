from itertools import count

sample = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".splitlines()


def drop(disks, delay):
    for t in count(delay, 1):
        # print ('time',t, 'capusle at level',t-delay)

        for n, disk in enumerate(disks, 1):
            # print(f'Disk #{n} has {disk[0]} positions; at time={t} it is at position {(disk[1]+t)%disk[0]}')
            if t - delay == n:
                if (disk[1] + t) % disk[0] != 0:
                    # if n > 5:
                    # 	print('capsule blocked', n, t, delay)
                    return False
        if t - delay > len(disks):
            return True
        # if t==1000: return -1


def solve(disks, delay=0, jump=1):
    while not drop(disks, delay):
        delay += jump
    return delay


def sample():
    disks = [(5, 4), (2, 1)]
    print("#sample", solve(disks))


def part1():
    disks = [(13, 11), (5, 0), (17, 11), (3, 0), (7, 2), (19, 17)]
    print("#1", solve(disks, 1, 13))


def part2():
    disks = [(13, 11), (5, 0), (17, 11), (3, 0), (7, 2), (19, 17), (11, 0)]
    print("#2", solve(disks, 1, 13))


if __name__ == "__main__":
    part1()
    part2()
