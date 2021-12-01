with open("in1.txt") as f:
    lines = [int(line) for line in f.readlines()]

    f.close()

    c = 0
    for i in range(len(lines)-1):
        if lines[i] < lines[i+1]:
            c += 1
    print(c)

    c = 0
    for i in range(len(lines)-3):
        if sum(lines[i:i+3]) < sum(lines[i+1:i+4]):
            c += 1
    print(c)
