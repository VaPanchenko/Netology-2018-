import os
import chardet


def get_file_list():

    file_dir = os.path.dirname(__file__)
    abs_file_dir = os.path.abspath(file_dir)
    migrations_path = os.path.join(abs_file_dir, 'Migrations')
    files = []
    for file in os.listdir(migrations_path):
        if file.endswith('.sql'):
            files.append(file)
    return files


def main(files):

    file_dir = os.path.dirname(__file__)
    abs_file_dir = os.path.abspath(file_dir)
    migrations_path = os.path.join(abs_file_dir, 'Migrations')
    while True:
        new_files = []
        line = str(input('\nВведите строку:'))
        for file in files:
            file_path = os.path.join(migrations_path, file)
            with open(file_path, 'rb') as f:
                data = f.read()
                r = chardet.detect(data)
                file_read = data.decode(encoding=r['encoding'])
            if line in file_read:
                new_files.append(file)
        if len(new_files) == 0:
            print('В файлах нет искомой строки -', line)
            break
        else:
            print('\nСтрока {} найдена в {} файлах\n'.format(line, len(new_files)))
            for i, file in enumerate(new_files, 1):
                print(i, file)
        files = new_files


main(get_file_list())
