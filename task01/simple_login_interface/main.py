# !/usr/bin/env python
# encoding: utf-8

import sys
import pandas as pd


def get_login_information():
    """
    读取表中存取的用户名密码
    :return:
    """
    get_data = pd.read_csv("basic_information", sep=" ")
    deal_data = get_data.groupby("username")["password"].apply(list).to_dict()
    return deal_data


def locking(username):
    """
    将要锁定的用户写入表
    :param username:
    :return:
    """
    with open("locking_user", mode='a+', encoding="utf-8") as w:
        w.write("\n" + username)
    return None


def get_locking_name(username):
    """
    获取锁定的用户名
    :param username:
    :return:
    """
    locking_name = open("locking_user", mode='r', encoding="utf-8").read().split("\n")
    flag = False
    for locked_name in locking_name:
        if username == locked_name:
            flag = True
    return flag


def login_judge_locked(locked_sige, username, password):
    """
    判断用户是否被锁定
    :return:
    """
    while locked_sige:
        print("该用户已锁定")
        username = input("请重新输入用户名：")
        password = input("请重新输入密码：")
        locked_sige = get_locking_name(username)
    return username, password


def login_judge_username(username, password):
    """
    判断用户名是否正确
    :return:
    """
    flag = False
    data_name = data.keys()
    while not flag:
        for i in data_name:
            if username == i:
                flag = True
        if not flag:
            username = input("无此用户，请重新输入用户名：")
            password = input("请重新输入密码：")
    return flag, username, password


def login_judge_password(flag, username, password):
    """
    判断密码是否正确, 多次错误锁定该用户
    :return:
    """
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
        login(username, password)
    return flag, username, password


def login(username, password):
    """
    判断输入的用户名密码是否正确
    :param username:
    :param password:
    :return:
    """
    locked_sige = get_locking_name(username)
    username, password = login_judge_locked(locked_sige, username, password)
    flag, username, password = login_judge_username(username, password)
    login_judge_password(flag, username, password)
    return None


if __name__ == '__main__':
    data = get_login_information()
    get_name = input("请输入用户名；")
    get_password = input("请输入密码：")
    login(get_name, get_password)
