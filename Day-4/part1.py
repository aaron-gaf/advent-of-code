import hashlib
import itertools
digest = ''
num = -1

for count in itertools.count():
    m = hashlib.md5()
    m.update('iwrupvqb' + str(count))
    digest = m.hexdigest()
    if (digest.startswith('00000')):
        num = count
        break;
print(num)
print(digest)