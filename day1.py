with open("in1.txt") as f:
    lines = f.readlines()
    f.close()

    c = 0
    for i in range(len(lines)-1):
        if int(lines[i]) < int(lines[i+1]):
            c += 1
    print(c)

    c = 0
    for i in range(len(lines)-3):
        if int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) < int(lines[i+1])+int(lines[i+2])+int(lines[i+3]):
            c += 1
    print(c)
