
input = []

with open("day3_input.txt") as file:
    input = [line[:-1] for line in file.readlines()]

lineSize = len(input[0])

gamma = ""
epsilon = ""
for p in range(lineSize):
    freq0 = len(list(filter(lambda x: x[p] == "0", input)))
    freq1 = len(list(filter(lambda x: x[p] == "1", input)))

    gamma += "0" if freq0 > freq1 else "1"
    epsilon += "1" if freq0 > freq1 else "0"

print(int(epsilon, 2) * int(gamma, 2))
print("*********")

workInput = input.copy()

while(len(workInput) > 1):
    for p in range(lineSize):
        freq0 = len(list(filter(lambda x: x[p] == "0", workInput)))
        freq1 = len(list(filter(lambda x: x[p] == "1", workInput)))

        c = "0" if freq0 > freq1 else "1"

        workInput = list(filter(lambda x: x[p] == c, workInput))

        # check if done before all positions are processed
        if(len(workInput) == 1):
            break

oxigen = int(workInput[0], 2)

workInput = input.copy()

while(len(workInput) > 1):
    for p in range(lineSize-1):
        freq0 = len(list(filter(lambda x: x[p] == "0", workInput)))
        freq1 = len(list(filter(lambda x: x[p] == "1", workInput)))

        c = "1" if freq1 < freq0 else "0"

        workInput = list(filter(lambda x: x[p] == c, workInput))

        # check if done before all positions are processed
        if(len(workInput) == 1):
            break

co2 = int(workInput[0], 2)

print(oxigen * co2)
