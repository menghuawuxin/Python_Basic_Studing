# !/usr/bin/env python
# encoding: utf-8

import sys
import pandas as pd


def get_login_information():
    get_data = pd.read_csv("basic_information", sep=" ")
    deal_data = get_data.groupby("username")["password"].apply(list).to_dict()
    return deal_data

def login(username, password, data):
    '''
    判断输入的用户名密码是否正确
    :param username:
    :param password:
    :return:
    '''
    flag = False
    data_name = data.keys()
    for i in data_name:
        if username == i:
            flag = True
    if flag and data[username][0] == password:
        return "0"
    else:
        return flag

def login_again(params, data):
    pass

if __name__ == '__main__':
    data = get_login_information()
    get_name = input("请输入用户名；")
    get_password = input("请输入密码：")
    get_login_data = login(get_name, get_password, data)
    if get_login_data == "0":
        print("成功登陆")
    else:
        print("登陆失败")
