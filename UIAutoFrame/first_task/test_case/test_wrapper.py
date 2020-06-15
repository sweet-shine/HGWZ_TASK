# coding=utf-8
# auther:wangc
# 2020-06-15

def wrapper(func):
    def hello():
        print('hello')
        func()
        print('good bye')
    return hello

@wrapper
def tmp():
    print('aaa')


if __name__ == '__main__':
    tmp()