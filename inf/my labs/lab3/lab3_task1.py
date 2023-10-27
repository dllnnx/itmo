# номер ису 408536, глаза-нос-рот: 202
import re

smile = 'X-O'
test1 = 'abcde' + smile + 'fg' + smile * 5 + '--OOOOXO-'
test2 = 'X--O' + 'X' + smile + '-0-0X' + smile
test3 = '----XXX000}{./' + smile * 3 + 'smileX_0 x-O'
test4 = 'X-o x-O x_0' + smile * 2 + 'X_O x-0 X-0' + smile * 2
test5 = 'X-O' + 'OOOXXX' + smile
tests = [test1, test2, test3, test4, test5]
for test in tests:
    print('test =', test)
    print(len(re.findall(smile, test)))
    print()
