import sys
input = []

with open("day7_input.txt") as file:
    input = [line
             for line in file.readlines()]

crabs = list(map(lambda x: int(x), input[0].split(",")))

cMax = max(crabs)
cMin = min(crabs)

eMin = sys.maxsize
lvl = -1
for i in range(cMin, cMax + 1):
    e = sum(map(lambda x: i - x, crabs))
    if(e < eMin):
        lvl = i
        eMin = e
        
print(eMin)

eMin = sys.maxsize
lvl = -1
for i in range(cMin, cMax + 1):
    e = sum(map(lambda x: (abs(i - x) * (abs(i - x) + 1)) / 2, crabs))
    if(e < eMin):
        lvl = i
        eMin = e

print(int(eMin))
