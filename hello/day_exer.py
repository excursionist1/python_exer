# 사용자로부터 data 입력 받는다.

def get_passwd_from_user():
   from_user = input('iuput your password:\n>>')
   return from_user

# validation check
def is_mixed(passwd):
    """
    패스워드의 적절성 검사
    :param passwd:입력값
    :return:bool로 리턴
    """
    numeric = False
    alpha = False
    special_char = False

    for char in passwd:
        if char.isalpha():
            alpha = True
        elif char.isnumeric():
            numeric = True
        else:
            special_char = True
    return (numeric and alpha) and special_char
    if passwd.isalpha():
        return False
    elif passwd.isalnum():
        return False
    elif passwd.isnumeric():
        return False
    else:
        return True




def main():

    passwd_from_user = get_passwd_from_user()

    if len(passwd_from_user) < 8:
        print('8자 이상 입력해주세요')
    elif not is_mixed(passwd_from_user):
        print('숫자 문자 특수문자가 1자 이상 포함되어야 합니다.')
    else:
        print('password를 입력 하였습니다.')



if __name__ == '__main__':
    main()