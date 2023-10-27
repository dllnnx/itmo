# вариант 2
import re

patterns = [re.compile('ВТ\s+ИТМО'), re.compile('ВТ(?:\s+\W*\w+\W*\s+\W*)ИТМО'), re.compile('ВТ\s+(?:\W*\w+\W*\s+\W*){2}ИТМО'), \
            re.compile('ВТ\s+(?:\W*\w+\W*\s+\W*){3}ИТМО'), re.compile('ВТ\s+(?:\W*\w+\W*\s+\W*){4}ИТМО')]

test1 = "ВТ          ИТМО?"
test2 = "ВТВТВТ ВТ ВТ кафедра в ИТМО?"
test3 = 'чтоооооо ВТ эт_о ___ лучшая кафедра ИТМО ИТМО ИТМОИТМО'
test4 = 'ВТ это ИТМО ИТМО это ВТ слово1 слово2 ИТМО ИТМО ВТ'
test5 = '////__ВТ слово1 слово2 слово3 слово4 слово5 ИТМО'

tests = [test1, test2, test3, test4, test5]
for test in tests:
    print('test = ', test)
    for pattern in patterns:
        if re.findall(pattern, test): print(*re.findall(pattern, test))
    print()
