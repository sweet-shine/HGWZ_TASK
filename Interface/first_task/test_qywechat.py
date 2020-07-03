# coding=utf-8
# auther:wangc
# 2020-07-03

import requests


# 获取token
def test_get_token():
    corpid = 'ww65cd3275dad0af38'
    corpsecret = 'ml7ZFg_LGtGK7g-mxwZ8rFbDnBG87JNPw2MtIxpkBgw'
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print(r.json()['access_token'])
    return r.json()['access_token']


# 创建部门
def test_department_create():
    payload = {
        "name": "广州研发中心111",
        "name_en": "RDGZ111",
        "parentid": 1,
        "order": 2,
    }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_get_token()}',
                      json=payload)
    print(r.json())

    # 获取返回的部门id
    create_department_id = r.json()['id']

    # 查询该部门id的信息是否存在
    department_list = test_department_list(create_department_id)['department']
    assert ((r.json()['errcode'] == 0) & (department_list[0]['id'] == create_department_id) & (
                department_list[0]['name'] == '广州研发中心111'))
    return create_department_id


# 更新部门
def test_department_update():
    payload = {
        "id": 2,
        "name": "广州研发中心333",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1
    }

    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_get_token()}',
                      json=payload)
    print(r.json())

    # 查询该部门id的信息是否存在
    department_list = test_department_list(2)['department']
    assert ((r.json()['errcode'] == 0) & (r.json()['errmsg'] == "updated") & (department_list[0]['name'] == '广州研发中心333'))


# 删除部门
def test_department_delete():
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_get_token()}&id=3')
    print(r.json())

    # 查询该部门id的信息是否存在
    res = test_department_list(3)
    assert ((r.json()['errcode'] == 0) & (r.json()['errmsg'] == "deleted") & (res['errcode'] == 60123) & (res['department'] == []))


# 获取部门列表，返回部门列表
def test_department_list(department_id=11):
    department_id = department_id
    r = requests.get(
        f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_get_token()}&id={department_id}')
    print(r.json())
    return r.json()
