import pyperclip
import sys



passwords = {
    'naver': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'daum': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'google': '12345',
}


def main():
    arg_list = sys.argv[1]

    if arg_list in passwords:
        pyperclip.copy(passwords[arg_list])
        print(arg_list, '의 비밀번호가 복사되었습니다.')
    else:
        print('해당 패스워드가 없습니다.')

main()