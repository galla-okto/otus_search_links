import csv
import json

def output_datas(input_answers, links):
    if input_answers['output_format'] == '1':   # console
        print(links)
    elif input_answers['output_format'] == '2':   # json
        print(json.dumps(links, sort_keys=True, indent=4))
    elif input_answers['output_format'] == '3':  # csv
        filename = 'D:\esult.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, ['theme', 'url'])
            w.writeheader()
            for link in links:
                w.writerow(link)
    else:
        print('Format isn''t supported')