def order_food():
    food_name = input("请输入订餐食物的名称")
    delivery_address = input("请输入送货地址")

    fast_food = ["汉堡", "薯条", "炸鸡", "奶茶"]
    cooking_food = ["火锅", "烧烤", "麻辣烫", "砂锅"]

    if food_name in fast_food:
        delivery_time = "30分钟内"
    elif food_name in cooking_food:
        delivery_time = "1小时内"
    else:
        delivery_time = "45分钟内"

    return f"你订购的{food_name}将在{delivery_time}\n送达您的地址:{delivery_address}"


print(order_food())
