import re
import time

nice = []

firstCheck = re.compile(r'([aeiou].*){3,}')
secondCheck = re.compile(r'(.)\1')
thirdCheck = re.compile(r'ab|cd|pq|xy')

with open('myinput.txt') as f:
    for line in f:
        if (firstCheck.search(line.rstrip('\n')) and secondCheck.search(line.rstrip('\n')) and not thirdCheck.search(line.rstrip('\n'))):
            nice.append(line.rstrip('\n'))
f.close()

print(str(len(nice)))