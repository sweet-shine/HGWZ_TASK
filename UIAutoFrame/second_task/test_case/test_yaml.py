# coding=utf-8
# auther:wangc
# 2020-06-18
import yaml


def test_yaml():
    with open('../page/search1.yaml', encoding='utf-8') as f:
        aa = yaml.safe_load(f)
        print(aa)