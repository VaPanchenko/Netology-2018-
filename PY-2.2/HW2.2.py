import chardet
import re


def get_list_from_file_txt(file):

    with open(file, 'rb') as f:
        data = f.read().strip()
        result = chardet.detect(data)
        file_list = re.split(r' ', data.decode(result['encoding']))
    return file_list


def get_len(file):

    from collections import Counter
    list = get_list_from_file_txt(file)
    print(list)
    new_list = []
    for world in list:
        if len(world) > 6:
            new_list.append(world)
    c = Counter(new_list).most_common(10)
    print('\nВ файле {}'.format(file), 'ТОП 10 слов длиной > 6 символов :')
    for i in range(10):
         print(c[i][0], c[i][1])


def main():
    get_len('newscy.txt')
    get_len('newsfr.txt')
    get_len('newsafr.txt')
    get_len('newsit.txt')

main()
