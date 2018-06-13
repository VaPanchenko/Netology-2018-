def get_path_files():
    import os
    file_dir = os.path.dirname(__file__)
    abs_file_dir = os.path.abspath(file_dir)
    files_sourse_path = os.path.join(abs_file_dir, 'Source')
    files_output_path = os.path.join(abs_file_dir, 'Result')
    return files_sourse_path, files_output_path


def get_file_list(files_path):
    import os
    files = []

    for file in os.listdir(files_path):
        if file.endswith('.jpg'):
            files.append(file)
    return files


def convert_jpg(files, files_path_result, files_path_sourse):
    import subprocess
    import os

    for file in files:
        subprocess.Popen(['sips', '--resampleWidth', '200', '--out', os.path.join(files_path_result, file), os.path.join(files_path_sourse, file)])


def main():
    import os
    files_path_sourse, files_path_result = get_path_files()
    files = get_file_list(files_path_sourse)
    if os.path.exists(files_path_result):
        pass
    else:
        os.mkdir(files_path_result)
    convert_jpg(files, files_path_result, files_path_sourse)


main()