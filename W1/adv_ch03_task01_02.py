import random

# 创建一个包含早餐食物的列表
breakfast = ['牛奶', '包子', '鸡蛋', '香蕉', '燕麦']

# 从列表中随机选择2样食物
favorite_breakfast = random.sample(breakfast, 3)

# 将选择的食物连接成一个字符串，并打印
print(f"我今天的早餐是：{', '.join(favorite_breakfast)}。")


# join 方法：join 是一个字符串方法，用于将序列（例如列表或元组）中的元素连接成一个字符串。序列中的每个元素都应该是字符串。
#
# ', '.join(favorite_breakfast)：
#
# ', '：这是连接序列元素的分隔符。在这种情况下，它是一个逗号和一个空格。
# favorite_breakfast：这是一个包含字符串元素的列表。
# ', '.join(favorite_breakfast)：join 方法将 favorite_breakfast 列表中的所有元素连接成一个新字符串。列表中的每个元素之间都插入了分隔符 ', '。
# {', '.join(favorite_breakfast)}：这个表达式被包含在花括号 {} 中，这通常用于字符串格式化（例如 f-字符串）。在这个例子中，它可能是f-字符串的一部分，用于将计算结果插入到一个更大的字符串中。
#
# 例如，如果 favorite_breakfast = ['牛奶', '包子', '鸡蛋']，那么 ', '.join(favorite_breakfast) 将返回字符串 "牛奶, 包子, 鸡蛋"。然后，这个字符串可以被插入到一个更大的字符串中，例如：