# -*-coding:utf-8-*-

my_dict = {'name': 'cheolwon', 'add': 'seoul', 'age': 33}

for item in my_dict:
    print(item)

for key in my_dict.keys():
    print(key)

for val in my_dict.values():
    print(val)

for key, val in my_dict.items():
    print(key, val)

for item in my_dict.items():
    print(type(item))