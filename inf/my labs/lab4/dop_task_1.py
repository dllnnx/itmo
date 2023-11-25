from json2xml import json2xml
from json2xml.utils import readfromjson

def main():
    input_file, output_file = "schedule.json", "schedule1.xml"
    with open(output_file, 'w', encoding='utf-8') as out_file:
        data = readfromjson(input_file)
        print(json2xml.Json2xml(data).to_xml(), file=out_file)

main()

