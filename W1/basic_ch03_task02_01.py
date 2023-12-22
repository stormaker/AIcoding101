# Task 2 程序结构
# 题目1: 用户身份验证程序
# 说明：要求用户输入用户名和口令（密码），然后程序进行验证。正确的用户名是admin，对应的密码是42。只有当用户名和密码都正确时，才提示“身份验证成功”，否则提示“身份验证失败”。
# 知识点：分支结构

user = "admin"
password = "42"

input_user = input("输入用户名")
input_password = input("输入密码")

if input_user == user and input_password == password:
    print("验证成功")
else:
    print("验证失败")
