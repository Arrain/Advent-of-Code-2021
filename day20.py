import numpy

input = []

with open("day20_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

trans = input[0]


def doWork(times):
    map = []
    for i in range(2, len(input)):
        row = [input[i][x] for x in range(len(input[i]))]
        map.append(row)

    img = numpy.asmatrix(map)
    for q in range(times):
        newImg = numpy.pad(
            img, 2, "constant", constant_values="." if q % 2 == 0 else "#"
        )
        newImgRez = numpy.pad(
            img, 2, "constant", constant_values="#" if q % 2 == 0 else "."
        )
        yMax = newImg.shape[0]
        xMax = newImg.shape[1]

        for y in range(1, yMax - 1):
            for x in range(1, xMax - 1):
                val = (
                    newImg[y - 1, x - 1]
                    + newImg[y - 1, x]
                    + newImg[y - 1, x + 1]
                    + newImg[y, x - 1]
                    + newImg[y, x]
                    + newImg[y, x + 1]
                    + newImg[y + 1, x - 1]
                    + newImg[y + 1, x]
                    + newImg[y + 1, x + 1]
                )
                val = int(val.replace(".", "0").replace("#", "1"), 2)
                newImgRez[y, x] = trans[val]
        img = newImgRez

    yMax = img.shape[0]
    xMax = img.shape[1]

    c = 0
    for y in range(1, yMax - 1):
        for x in range(1, xMax - 1):
            if img[y, x] == "#":
                c += 1
    print(c)


doWork(2)
doWork(50)
