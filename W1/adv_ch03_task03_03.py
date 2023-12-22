def movie_plan(friend_names, movie_list):
    movie_choices = {}  # 创建一个空字典，用于存储朋友们的电影选择

    for friend in friend_names:  # 遍历朋友名字列表
        print(f"Hello, {friend}! 以下是可供选择的电影：")

        # 显示电影列表，让朋友选择
        for i, movie in enumerate(movie_list, 1):
            print(f"{i}. {movie}")

        while True:  # 保证朋友输入一个有效的选择
            choice = input(f"{friend}，请问你想看哪部电影？ (请输入数字)：")
            if choice.isdigit() and 1 <= int(choice) <= len(movie_list):
                chosen_movie = movie_list[int(choice) - 1]  # 获取朋友选择的电影
                movie_choices[friend] = chosen_movie  # 将选择保存到字典中
                print(f"{friend} 选择了 {chosen_movie}\n")
                break
            else:
                print("输入无效，请输入电影前面的数字。")

    return movie_choices  # 返回包含朋友们电影选择的字典


# 示例输入
friend_names = ['张三', '李四', '王五']
movie_list = ['流浪地球', '复仇者联盟', '哪吒之魔童降世']

# 调用函数并打印输出
print(movie_plan(friend_names, movie_list))
