
def get_string_data_file(file):

    import json
    import chardet

    with open(file, 'rb') as f:
        data = f.read ()
        r = chardet.detect(data)

    with open(file, encoding=r['encoding']) as f:
        string_data = ''
        file = json.load(f)
        rss_key = file.get('rss')
        chanel_key = rss_key.get('channel')
        string_data += chanel_key.get('description')
        items_key = chanel_key.get('items')
        for i in items_key:
            value = i.get('description')
            string_data += value
    return string_data


def get_len(file):
    import re
    from collections import Counter

    new_list = []
    list = re.split(r' ', get_string_data_file(file))

    for world in list:
        if len(world) > 6:
            new_list.append(world)
    c = Counter(new_list).most_common(10)
    print ('\nВ файле {}'.format(file), 'ТОП 10 слов длиной > 6 символов :')
    for i in range(10):
         print(c[i][0], c[i][1])


def main():
    get_len('newsafr.json')
    get_len('newscy.json')
    get_len('newsfr.json')
    get_len('newsit.json')

main()


