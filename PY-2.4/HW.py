def get_file_list():
    import os
    file_dir = os.path.dirname(__file__)
    abs_file_dir = os.path.abspath(file_dir)
    migrations_path = os.path.join(abs_file_dir, 'Migrations')
    files = []
    for file in os.listdir(migrations_path):
        if file.endswith('.sql'):
            files.append(file)
    return files


def main(files):
    import os
    import chardet
    file_dir = os.path.dirname(__file__)
    abs_file_dir = os.path.abspath(file_dir)
    migrations_path = os.path.join(abs_file_dir, 'Migrations')
    while True:
        new_files = []
        line = str(input('Введите строку:'))
        for file in files:
            file_path = os.path.join(migrations_path, file)
            with open(file_path, 'rb') as f:
                data = f.read ()
                r = chardet.detect(data)
            with open(file_path, encoding=r['encoding']) as f:
                file_read = f.read()
            if line in file_read:
                new_files.append(file)
        if len(new_files) == 0:
            print('В файлах нет искомой строки -', line)
            break
        else:
            print(new_files)
            print('Строка', line, 'найдела в ', len(new_files), 'файлах')
        files = new_files


main(get_file_list())

