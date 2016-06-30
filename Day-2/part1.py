#make an array with all of the puzzle input
puzzleInput = []
totalArea = 0

with open('myinput.txt') as f:
    for line in f:
        puzzleInput.append(line)
f.close()

#set them all to none for now
lw=wh=hl=area=smallest = None
for line in puzzleInput:
    temp = line.split('x')
    lw = int(temp[0]) * int(temp[1])
    wh = int(temp[1]) * int(temp[2])
    hl = int(temp[2] )* int(temp[0])
    area = (2 * lw) + (2 * wh) + (2 * hl)
    smallest = min(lw, wh, hl)
    area += smallest
    totalArea += area
print(str(totalArea) + ' square feet of wrapping paper needs to be ordered!')