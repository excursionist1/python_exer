# -*-coding:utf-8-*-

def time(a=10, b=20):
    return a * b

x = time()

y = time(5)

print(x)
print(y)

def var_param_test(*p):
    return p

a = var_param_test(1,2,3,4,5)

print(a)
print(type(a))


def tuple_return_test():
    return 3, 5, 'hello'

def main():
    ret = tuple_return_test()

    print(type(ret))
    print(ret)
main()

