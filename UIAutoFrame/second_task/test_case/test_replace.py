import json


def test_replace():
    steps = {"name" : 'fsdfsdfsdkjlsdf${stock_name}dsfjsldkfjsdoi'}
    # str1 = 'fsdfsdfsdkjlsdf${stock_name}dsfjsldkfjsdoi'
    raw = json.dumps(steps)
    if '${stock_name}' in raw:
        raw = raw.replace('${stock_name}', '11212121')
        print(raw)

    steps = json.loads(raw)
    print(steps)
    print(type(steps))