# -*-coding:utf-8-*-

# list

my_list = ['banana','apple','pear','berry','apple']

a = my_list[0]
b = my_list[1:3]

print(my_list.count('apple'))
my_list.sort()

# if / else 문
exist_banana = 'banana' in my_list
print(exist_banana)

if 'banana' in my_list:
    print('바나나가 있네요')
else:
    print('바나나 없어요')

# 리스트 element 추가
my_list.append('mango')
my_list[1] = 'pineapple'

# 리스트 element 삭제 (remove, del)
del my_list[1]
my_list.remove('banana')

print(my_list)

# for문 예제
for item in my_list:
    print(item)

print('OUT OF FOR')

# list : 1차원 형태의 시퀀스 데이터 (Read/Write)
# Read Only List : Tuple -> Read only이기 때문에 빠르다.

a, b, c = ('apple', 'pear', 'banana')  # unpacking
print(a)
print(b)
print(c)

# dict 아이템 추가와 업데이트
slang = {}
slang['cheerio'] = 'goodbye'
slang['cheerio'] = 'hello'
slang['smashing'] = 'tennis'
del slang['cheerio']

print(slang)
