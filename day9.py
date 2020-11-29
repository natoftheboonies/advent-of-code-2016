def parse(puzzle):
    pos = 0
    count = 0
    while pos < len(puzzle):
        if puzzle[pos] == "(":
            end = puzzle.index(")", pos)
            chars, repeat = map(int, puzzle[pos + 1 : end].split("x"))

            pos = end + chars
            count += chars * repeat - 1
        else:
            pos += 1
            count += 1
    return count


ex1 = "A(1x5)BC"
assert parse(ex1) == 7

ex2 = "(3x3)XYZ"
assert parse(ex2) == 9

ex3 = "A(2x2)BCD(2x2)EFG"
assert parse(ex3) == 11

ex4 = "(6x1)(1x3)A"
assert parse(ex4) == 6

assert parse("X(8x2)(3x3)ABCY") == 18

with open("input9") as fp:
    print("#1", parse(fp.read().strip()))


def parse2(puzzle):
    pos = 0
    count = 0
    while pos < len(puzzle):
        if puzzle[pos] == "(":
            end = puzzle.index(")", pos)
            chars, repeat = map(int, puzzle[pos + 1 : end].split("x"))
            repeat_chars = puzzle[end + 1 : end + chars + 1]
            expand = parse2(repeat_chars)
            # print('recurse',repeat_chars,expand)
            count += repeat * expand - 1
            pos = end + chars
        else:
            pos += 1
            count += 1
    return count


assert parse2("X(8x2)(3x3)ABCY") == 20
# X(3x3)ABC(3x3)ABC(3x3)ABCY

assert parse2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920

assert parse2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445

with open("input9") as fp:
    print("#2", parse2(fp.read().strip()))
