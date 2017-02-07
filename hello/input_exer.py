# -*-coding:utf-8-*-
post_fix = 'aay'

original = input('input your text\n>>')

if len(original) > 0 and original.isalpha():
    first_char = original[0]
    new_word = original[1:] + first_char + post_fix
    print(new_word)
else:
    print('invalid word')

