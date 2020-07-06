# coding=utf-8
# auther:wangc
# 2020-07-03
import pytest
import requests


# 获取token
@pytest.fixture(scope='session')
def test_get_token():
    corpid = 'ww65cd3275dad0af38'
    corpsecret = 'ml7ZFg_LGtGK7g-mxwZ8rFbDnBG87JNPw2MtIxpkBgw'
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print(r.json()['access_token'])
    return r.json()['access_token']


# 创建部门
def test_department_create(name, test_get_token):
    payload = {
        "name": name,
        "parentid": 1
    }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_get_token}',
                      json=payload)
    print(r.json())
    return r.json()


# 更新部门
def test_department_update(department_id, department_name, test_get_token):
    payload = {
        "id": department_id,
        "name": department_name
    }

    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_get_token}',
                      json=payload)
    print(r.json())
    return r.json()


# 删除部门
def test_department_delete(department_id, test_get_token):
    r = requests.get(
        f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_get_token}&id={department_id}')
    print(r.json())
    return r.json()


# 获取部门列表，返回部门列表
def test_department_list(test_get_token, department_id=1):
    r = requests.get(
        f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_get_token}&id={department_id}')
    print(r.json())
    return r.json()


@pytest.mark.parametrize('department_name', ["测试部门0706" + str(x) for x in range(1, 30)])
def test_all(test_get_token, department_name):
    try:
        # 可能会存在部门名称已存在的异常
        creat_res = test_department_create(department_name, test_get_token)
        assert 'created' == creat_res['errmsg']
    except AssertionError as e:
        # 如果异常信息中有部门已存在的信息，则进行处理
        if "department existed" in e.__str__():
            # 获取所有部门信息，遍历，如果有部门名称与参数的部门名称相同，则执行删除对应id的方法
            department_list = test_department_list(test_get_token)["department"]
            for department in department_list:
                if department_name == department["name"]:
                    test_department_delete(department["id"])
    new_department_name = '111' + department_name
    assert "updated" == test_department_update(creat_res['id'], new_department_name, test_get_token)['errmsg']
    assert new_department_name == test_department_list(test_get_token, creat_res['id'])["department"][0]["name"]
    assert "deleted" == test_department_delete(creat_res['id'], test_get_token)['errmsg']
