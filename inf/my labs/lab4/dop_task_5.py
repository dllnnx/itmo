def dict_to_csv(d: dict, delimiter=','):
    text_csv = ''
    keys = ['lesson number'] + list(d['lesson1'].keys())
    text_csv += delimiter.join(map(parse, keys)) + '\n'
    for k, v in d.items():
        values = [k] + list(d[k].values())
        text_csv += delimiter.join(map(parse, values)) + '\n'
    return text_csv

def parse(v):
    if isinstance(v, str): return f'"{v}"'
    return str(v).replace(',', ';')

def main():
    input_file, output_file = "schedule1.json", "schedule.csv"
    with open(input_file, 'r', encoding='utf-8') as in_file, \
        open(output_file, 'w', encoding='utf-8') as out_file:
        text = in_file.read()
        d = eval(text)
        print(dict_to_csv(d), file=out_file)

main()
