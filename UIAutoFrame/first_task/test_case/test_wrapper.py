# # coding=utf-8
# # auther:wangc
# # 2020-06-15
#
# def wrapper(func):
#     a = 1
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


_black_list = ['资金', '确定', '确认', '取消', '是', '下次再说']
for i in _black_list:
    print(i)