# coding=utf-8
# auther:wangc
# 2020-06-18


# def test_repr():
#     list1 = [1,2,3,4,5]
#     dict1 = {"name":"tome",
#              "age": 10,
#              "sex": "male"}
#
#     print(list1,dict1)
#     print(repr(list1),repr(dict1))
#     print(type(repr(list1)),type(repr(dict1)))

def tnonlocal(func):
    a = 5
    def aaa():
        func()
        nonlocal a
        a += 1
        print(a)
    # print(a)
    return aaa

@tnonlocal
def test_b():
    print('bbb')

# test_b()