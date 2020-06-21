import inspect


def a():
    print(inspect.stack()[1].function)
    print("aaa")

def test_inspect():
    a()
