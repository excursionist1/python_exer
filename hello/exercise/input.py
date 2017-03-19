my_age = input('나이 입력:\n>>')

if my_age.isnumeric():
# 문자를 숫자로 바꿔줌
    my_int_age = int(my_age)
else:
    my_int_age = 0


if my_int_age >= 18:
    print('성인')
else:
    print('미성년')