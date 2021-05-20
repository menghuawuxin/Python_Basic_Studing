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

    locked_sige = get_locking_name(username)
    while locked_sige:
        print("该用户已锁定")
        username = input("请重新输入用户名：")
        password = input("请重新输入密码：")
        locked_sige = get_locking_name(username)
    flag = False
    data_name = data.keys()
    while not flag:
        for i in data_name:
            if username == i:
                flag = True
        if not flag:
            username = input("无此用户，请重新输入用户名：")
            password = input("请重新输入密码：")
    if flag and data[username][0] == password:
        print("欢迎登陆")
        sys.exit()
    else:
        for i in range(3):
            password = input("密码错误，请重新输入：")
            if data[username][0] == password:
                print("欢迎登陆")
                sys.exit()
            else:
                continue
        locking(username)
        username = input("密码多次错误，该用户被锁定，请重新输入用户名：")
        password = input("请输入密码：")
        login(username, password, data)
        return flag


def locking(username):
    with open("locking_user", mode='a+', encoding="utf-8") as w:
        w.write("\n" + username)
    return None


def get_locking_name(username):
    locking_name = open("locking_user", mode='r', encoding="utf-8").read().split("\n")
    flag = False
    for locked_name in locking_name:
        if username == locked_name:
            flag = True
    return flag


if __name__ == '__main__':
    data = get_login_information()
    get_name = input("请输入用户名；")
    get_password = input("请输入密码：")
    get_login_data = login(get_name, get_password, data)
