

def part1():

    def decode(key):
        x,y = key
        if y == -1:
            if x == -1:
                return 1
            if x == 0:
                return 2
            if x == 1:
                return 3
        if y == 0:
            if x == -1:
                return 4
            if x == 0:
                return 5
            if x == 1:
                return 6
        if y == 1:
            if x == -1:
                return 7
            if x == 0:
                return 8
            if x == 1:
                return 9

    assert decode((0,0))==5

    def follow(key, moves):
        x,y = key
        for move in moves:
            if move == 'U' and y > -1:
                y = y-1
            elif move == 'D' and y < 1:
                y = y+1
            elif move == 'L' and x > -1:
                x = x-1
            elif move == 'R' and x < 1:
                x = x+1
        return (x,y)

    assert follow((0,0),'ULL') == (-1,-1)
    assert follow((1,1),'LURDL') == (0,1)

    sample = '''ULL
    RRDDD
    LURDL
    UUUUD'''.splitlines()

    with open('input2', 'r') as fp:
        sample = [line.strip() for line in fp.readlines()]

    key = (0,0)
    result = ''
    for line in sample:
        key = follow(key, line)
        #print(key)
        result += str(decode(key))
    print('#1',result)


def part2():
    """
    2,0

    1,0 1,1

    0,0 0,1 0,2

    so, sum must be <= 2

    """

    def decode(key):
        x,y = key
        if y == -2:
            if x == 0:
                return 1
        if y == -1:
            if x == -1:
                return 2
            if x == 0:
                return 3
            if x == 1:
                return 4
        if y == 0:
            if x == -2:
                return 5
            if x == -1:
                return 6
            if x == 0:
                return 7
            if x == 1:
                return 8
            if x == 2:
                return 9
        if y == 1:
            if x == -1:
                return 'A'
            if x == 0:
                return 'B'
            if x == 1:
                return 'C'
        if y == 2:
            if x == 0:
                return 'D'
        # invalid coords
        print('invalid', key)
        return 'X'

    def follow(key, moves):
        x,y = key
        for move in moves:
            if move == 'U' and abs(x) < 2 and y > (-1 if abs(x) == 1 else -2):
                y = y-1
            elif move == 'D' and abs(x) < 2 and y < (1 if abs(x) == 1 else 2):
                y = y+1
            elif move == 'L' and abs(y) < 2 and x > (-1 if abs(y) == 1 else -2):
                x = x-1
            elif move == 'R' and abs(y) < 2 and x < (1 if abs(y) == 1 else 2):
                x = x+1
            #print(move,(x,y))
        return (x,y)

    sample = '''ULL
    RRDDD
    LURDL
    UUUUD'''.splitlines()

    with open('input2','r') as fp:
        sample = [line.strip() for line in fp.readlines()]

    key = (-2,0)
    result = ''
    for line in sample:
        key = follow(key, line)
        #print(key)
        result += str(decode(key))
    print('#2',result)

if __name__ == '__main__':
    part1()
    part2()