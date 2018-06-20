import requests
import os
import chardet


def get_path_files():
    file_dir = os.path.dirname(__file__)
    abs_file_dir = os.path.abspath(file_dir)
    files_sourse_path = os.path.join(abs_file_dir, 'Source')
    files_output_path = os.path.join(abs_file_dir, 'Result')
    return files_sourse_path, files_output_path


def get_file_list():
    files_path_sourse, files_path_result = get_path_files()
    files = []
    for file in os.listdir(files_path_sourse):
        if file.endswith('.txt'):
            files.append(file)
    return files


def read_file(file):
    files_path_sourse, files_path_result = get_path_files()
    file_path = os.path.join(files_path_sourse, file)
    with open(file_path, 'rb') as f:
        data = f.read()
        r = chardet.detect(data)
        file_read = data.decode(encoding=r['encoding'])
    return file_read


def translate_it(file_read, leng, file_for_translate):

    files_path_sourse, files_path_result = get_path_files()
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': leng,
        'text': file_read,
    }
    response = requests.get(url, params=params).json()
    translate = ' '.join(response.get('text', []))
    output_file = os.path.join(files_path_result, '{}-{}.txt'.format(file_for_translate, leng))
    print(output_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translate)


def main():
    files = get_file_list()
    for i, file in enumerate(files, 1):
        print(i, file)
    file_for_translate = str(input('Введите название файла для перевода:'))
    c = read_file(file_for_translate)
    leng_sourse = str(input('Введите язык оригинального текста (de(немецкий)/es(испанский)/fr(французкий):'))
    leng_dest = str(input('Введите язык перевода:'))
    leng = leng_sourse + '-' + leng_dest
    return translate_it(c, leng, file_for_translate)


main()



