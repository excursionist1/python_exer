# -*-coding:utf-8-*-

word_dict = {}

my_word = 'It was a bright cold day in April, and the clocks were striking thirteen.'

for item in my_word:
    word_dict.setdefault(item, 0)
    # TODO
    word_dict[item] = word_dict[item] + 1

print (word_dict)


