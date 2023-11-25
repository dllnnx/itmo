def main():
    with open("two_day_schedule.json", 'r', encoding='utf8') as in_file:
        data = in_file.readlines()[1:-1]
        lines_cnt = len(data)

    out_file = open("schedule3.xml", 'w', encoding='utf8')
    out_file.write('<?xml version="1.0" encoding="utf-8"?>')
    out_file.write('\n<root>')

    # убираем [ и { в отдельные строки
    for i in range(lines_cnt):
        if '{' in data[i] and '\n{' not in data[i]: data[i] = data[i].replace('{', '\n{')
        if '[' in data[i] and '\n[' not in data[i]: data[i] = data[i].replace('[', '\n[')

    # заново делю на строки, т.к. добавила \n
    all_data = ''
    for line in data: all_data += line # склеили все в одну строку
    data = all_data.split('\n') # разделили на строчки

    data = [line for line in data if line.strip() != ''] # удалили пустые строчки

    tabs_cnt = 1
    par_tags = []
    arr_tags = []
    lines_cnt = len(data)
    for i in range(lines_cnt):
        line = data[i]
        if line.strip() == '': continue

        # выделяем тег xml
        quote = line.find('\"')
        line = line.replace('\"', '')
        tag = line[quote : line.find(':')]
        if len(tag) > 0: tags = ['<' + tag + '> ', '</' + tag + '> ']

        # выделяем саму строчку (value)
        xml_line = line[line.find(':') + 1:].strip()

        if len(xml_line) > 0 and xml_line not in [ '{', '}', '[', ']', '},', '],']:
            if xml_line[-1] == ',': xml_line = xml_line[:-1] # убираем запятую в конце строки (если есть)
            out_file.write('\n' + tabs_cnt * '\t' + tags[0] + xml_line + tags[1]) # записываем "простую" строчку

        elif xml_line == '{':
            if data[i-1].strip() not in ['},', '[']:
                par_tags += [tags]
                out_file.write('\n' + tabs_cnt * '\t' + par_tags[-1][0])
                tabs_cnt += 1
            elif data[i-1].strip() == '},':
                out_file.write('\n' + tabs_cnt * '\t' + arr_tags[-1][0])
                tabs_cnt += 1

        elif xml_line == '[':
            arr_tags += [tags]
            out_file.write('\n' + tabs_cnt * '\t' + arr_tags[-1][0])
            tabs_cnt += 1

        elif xml_line == '},':
            tabs_cnt -= 1
            if data[i+1].strip() == '{': # если мы переходим к след эл-ту массива
                out_file.write('\n' + tabs_cnt * '\t' + arr_tags[-1][1])
            else: # если мы закончили какой-то блок
                out_file.write('\n' + tabs_cnt * '\t' + par_tags[-1][1])
                par_tags.pop(-1)

        elif xml_line == ']': # если мы закончили массив
            arr_tags.pop(-1) # удаляем тег массива

        elif xml_line == '}':
            if data[i+1].strip() == ']':
                tabs_cnt -= 1
                out_file.write('\n' + tabs_cnt * '\t' + arr_tags[-1][1])

    out_file.write('\n</root>')

main()