#make an array with all of the puzzle input
puzzleInput = []
totalRibbon = 0

with open('myinput.txt') as f:
    for line in f:
        puzzleInput.append(line)
f.close()

#set them all to none for now
num1=num2=num3=biggestDim = 0
for line in puzzleInput:
    temp = line.split('x')
    biggestDim = max(int(temp[0]), int(temp[1]), int(temp[2]))
    if biggestDim == int(temp[0]):
        num1 = (2 * int(temp[1])) + (2 * int(temp[2]))
    elif biggestDim == int(temp[2]):
        num1 = (2 * int(temp[0])) + (2 * int(temp[1]))
    else:
        num1 = (2 * int(temp[0])) + (2 * int(temp[2]))
    num2 = int(temp[0] ) * int(temp[1]) * int(temp[2])
    num3 = num1 + num2
    totalRibbon += num3
print(str(totalRibbon) + ' total feet of ribbon needs to be ordered!')