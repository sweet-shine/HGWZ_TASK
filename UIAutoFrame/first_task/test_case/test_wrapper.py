# # coding=utf-8
# # auther:wangc
# # 2020-06-15
#
# from functools import wraps
#
# def wrapper(func):
#     a = 1
#     @wraps(func)
#     def hello():
#         nonlocal a
#         print('hello')
#         func()
#         a += 1
#         print(a)
#         print('good bye')
#     print(a+5)
#     return hello
#
# @wrapper
# def tmp():
#     print('aaa')
#
#
# if __name__ == '__main__':
#     tmp()
#     print(tmp)

# _black_list = ['资金', '确定', '确认', '取消', '是', '下次再说']
# for i in _black_list:
#     print(i)
# def wrapper(func):
#     def doSomethingBeforeHi():
#         print("I am doing some boring work before executing hi()")
#         print(func())
#     return doSomethingBeforeHi
#
# @wrapper
# def hi():
#     return "hi yasoob!"
#
# print(hi)