
input = []

with open("day8_input.txt") as file:
    input = [line[:-1].split(" | ")
             for line in file.readlines()]

outs = list(map(lambda x: x[1].split(" "), input))

c = 0
for i in outs:
    c += sum(map(lambda x: len(x) in {2, 3, 4, 7}, i))

print(c)

v = 0
ins = list(map(lambda x: x[0].split(" "), input))

for ind, i in enumerate(ins):
    one = "".join(sorted(list(filter(lambda x: len(x) == 2, i))[0]))
    seven = "".join(sorted(list(filter(lambda x: len(x) == 3, i))[0]))
    four = "".join(sorted(list(filter(lambda x: len(x) == 4, i))[0]))
    eight = "".join(sorted(list(filter(lambda x: len(x) == 7, i))[0]))

    fivelen = list(filter(lambda x: len(x) == 5, i))
    sixlen = list(filter(lambda x: len(x) == 6, i))

    # get six
    for x in sixlen:
        f = False
        for y in one:
            if x.count(y) == 0:
                f = True
                break
        if f:
            sixlen.remove(x)
            six = "".join(sorted(x))
            break

    # get zero
    for x in sixlen:
        f = False
        for y in four:
            if x.count(y) == 0:
                f = True
                break
        if f:
            sixlen.remove(x)
            zero = "".join(sorted(x))
            break

    nine = "".join(sorted(sixlen[0]))

    # get seven
    for x in fivelen:
        f = True
        for y in seven:
            if x.count(y) == 0:
                f = False
                break
        if f:
            fivelen.remove(x)
            three = "".join(sorted(x))
            break

    # get five
    for x in fivelen:
        f = 0
        for y in four:
            if x.count(y) == 1:
                f += 1

        if f == 3:
            fivelen.remove(x)
            five = "".join(sorted(x))
            break

    two = "".join(sorted(fivelen[0]))

    # process out
    val = 0
    for j in outs[ind]:
        val *= 10
        s = "".join(sorted(j))
        if s == one:
            val += 1
        elif s == two:
            val += 2
        elif s == three:
            val += 3
        elif s == four:
            val += 4
        elif s == five:
            val += 5
        elif s == six:
            val += 6
        elif s == seven:
            val += 7
        elif s == eight:
            val += 8
        elif s == nine:
            val += 9
        else:
            val += 0

    v += val

print(v)
