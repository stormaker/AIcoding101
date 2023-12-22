# 题目2:输出斐波那契数列前20个数
# 说明：斐波那契数列（Fibonacci sequence），通常也被称作黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中研究在理想假设条件下兔子成长率问题而引入的数列，因此这个数列也常被戏称为“兔子数列”。斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，按照这个规律，斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
# 知识点： 循环结构

# 定义一个列表，初始包含斐波那契数列的前两个数字
fibonacci_numbers = [1, 1]

# 通过循环计算斐波那契数列的前20个数字
for i in range(2, 20): #i取值依次是2到20
 #   print(i,"-",fibonacci_numbers) 测试当前i值的斐波那契数列
    next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    # 下一个斐波那契数列的数字，是当前数列中最后第一个和倒数第二个元素之和
    fibonacci_numbers.append(next_number)
    # 在当前的数列在中，增加下一个数字

# 输出斐波那契数列
print("斐波那契数列的前20个数字：")
print(fibonacci_numbers)