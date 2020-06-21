import yaml

def test_yaml():
    with open('../data/stock_name.yaml', encoding='utf-8') as f:
        res = yaml.safe_load(f)
        print(res)