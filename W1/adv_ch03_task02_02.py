import random

number_to_guess= random.randint(1,100)
count = 0
print("欢迎进入猜数字游戏，请输入1-100的整数")

while True:
    user_guess=input("请输入你猜的数字：")

    # 检查用户输入是否为数字
    if not user_guess.isdigit():
        print("请输入一个有效的数字！")
        continue

    user_guess= int(user_guess)
    count= count+1

    if user_guess<number_to_guess:
        print(f"数字小了")
    elif user_guess>number_to_guess:
        print("数字大了")
    else:
        print(f"恭喜你猜对了，数字是{user_guess}，你一共猜了{count}次")
        break
