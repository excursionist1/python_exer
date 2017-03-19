import os
import glob

def rm_all_txt(dir_list):
    os.chdir(dir_list)
    print('change to', os.getcwd())
    for file_name in glob.glob('*'):
        if file_name.endswith('.txt'):
            os.remove(file_name)
            print(file_name, 'deleted')

    os.chdir('..')
    print('change to', os.getcwd())


os.chdir('Intro to Data Analysis subtitles')
for dir_list in glob.glob('*'):
    rm_all_txt(dir_list)








