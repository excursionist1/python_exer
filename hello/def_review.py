# -*-coding:utf-8-*-
import math

def shut_down(s):
    if s == 'yes':
        return 'Shutting down'
    elif s == 'no':
        return 'Shutdown aborted'
    else:
        return 'sorry'


def my_sqrt(data):
    return math.sqrt(data)


def distance_from_zero(data=3, second=2):
    if type(data) == int or type(data) == float:
        return abs(data)
    else:
        return 'nope'

def main():
    ret = distance_from_zero()
    print(ret, end=' ')
    print('program ended')

main()

