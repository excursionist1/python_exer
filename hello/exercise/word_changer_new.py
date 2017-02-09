# -*-coding:utf-8-*-

def get_data_from_user():
    return input('input your text\n>>')


def convert(original, post_fix):
    if len(original) > 0 and original.isalpha():
        first_char = original[0]
        new_word = original[1:] + first_char + post_fix
        return new_word
    else:
        return 'invalid word'
    return


def main():

    post_fix = 'jaask'

    original = get_data_from_user()

    converted = convert(original, post_fix)
    print(converted)

if __name__ == '__main__':
    main()
    #print('이 모듈은 실행파일이 아닙니다')