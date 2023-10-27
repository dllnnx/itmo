import re

def task3 (text):
    words = re.findall(r'\w+', text)
    one_vowel = []
    for word in words:
        for vowel in ['Аа', 'Ее', 'Ёё', 'Ии', 'Оо', 'Уу', 'Ыы', 'Ээ', 'Юю', 'Яя']:
            x = re.sub(f'[{vowel}]', '', 'АЕЁИОУЫЭЮЯаеёиоуыэюя')
            if re.search(rf"^[^{x}]*[{vowel}]+[^{x}]*$", word):
                one_vowel.append(word)

    return sorted(one_vowel, key=lambda x: (len(x), x))

test1 = "слова в которых разные гласные"
test2 = "погода была пасмурная, шел дождь"
test3 = "сколько слов с одной гласной"
test4 = "хорОшО плОхо информатика слово"
test5 = "какой бы тест ещё еще придумать"

tests = [test1, test2, test3, test4, test5]
for test in tests:
    print(*task3(test))
