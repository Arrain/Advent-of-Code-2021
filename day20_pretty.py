import numpy

input = []

with open("day20_input.txt") as file:
    input = [line.strip() for line in file.readlines()]


trans = input[0]


def doWork(times):
    map = [[input[i][x] for x in range(len(input[i]))] for i in range(2, len(input))]

    img = numpy.asmatrix(map)

    for q in range(times):
        newImg = numpy.pad(
            img, 2, "constant", constant_values=(trans[-1] if q % 2 == 0 else trans[0])
        )
        newImgRez = numpy.pad(
            img, 2, "constant", constant_values=(trans[0] if q % 2 == 0 else trans[-1])
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
                newImgRez[y, x] = trans[int(val.replace(".", "0").replace("#", "1"), 2)]
        img = newImgRez

    print(numpy.count_nonzero(img == "#"))


doWork(2)
doWork(50)
