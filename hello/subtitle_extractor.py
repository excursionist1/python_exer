import glob
import os

def delete_all_working_file(delete_target):
    for file_name in glob.glob('*'):
        if file_name.endswith(delete_target):
            os.remove(file_name)

def get_subtitle_file_list():
    os.chdir('Intro to Data Analysis Subtiltes')
    os.chdir('Lesson 1_ Data Analysis Process')
    delete_all_working_file('.txt')
    return glob.glob('*')

def create_new_subtitle_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.readlines()

    for item in contents:
        if item.count(':') > 3 and '-->' in item:
            contents.remove(item)
            continue

        if item.strip().isnumeric():
            contents.remove(item)
    with open(file_name, + '.txt', 'w') as output:
        output.writelines(contents)

    return file_name + '.txt'

def main():
    file_list = get_subtitle_file_list()

    for file in file_list:
        if file.endswith('.srt'):
            new_file_name = create_new_subtitle_file(file)
            print(new_file_name, 'created')
main()
