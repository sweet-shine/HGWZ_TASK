# coding=utf-8
# auther:wangc
# 2020-06-18


def test_repr():
    list1 = [1,2,3,4,5]
    dict1 = {"name":"tome",
             "age": 10,
             "sex": "male"}

    print(list1,dict1)
    print(repr(list1),repr(dict1))
    print(type(repr(list1)),type(repr(dict1)))