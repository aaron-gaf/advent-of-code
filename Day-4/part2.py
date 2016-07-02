import hashlib
import itertools
digest = ''
num = -1

for count in itertools.count():
    m = hashlib.md5()
    m.update('iwrupvqb' + str(count))
    digest = m.hexdigest()
    if (digest.startswith('000000')):
        num = count
        break;
print(num)
print(digest)