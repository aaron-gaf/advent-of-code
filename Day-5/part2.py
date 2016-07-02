import re
import time

nice = []

firstCheck = re.compile(r'(..).*\1')
secondCheck = re.compile(r'(.).\1')

with open('myinput.txt') as f:
    for line in f:
        if (firstCheck.search(line.rstrip('\n')) and secondCheck.search(line.rstrip('\n'))):
            nice.append(line.rstrip('\n'))
f.close()

print(str(len(nice)))