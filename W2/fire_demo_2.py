# fire_demo_2.py
# 导入fire库，用于快速地创建命令行接口
import fire

class Calculator(object):
    """A simple calculator class."""

    # 定义double方法，返回给定数字的两倍
    def double(self, number):
        return 2 * number

    # 定义add方法，返回两个数字的和
    def add(self, a, b):
        return a + b

    # 定义multiply方法，返回两个数字的乘积
    def multiply(self, a, b):
        return a * b

    # 定义minus方法，返回第一个数字减去第二个数字的结果
    def minus(self, a, b):
        return a - b

# 确保只有在直接运行这个脚本时才执行下面的代码
if __name__ == '__main__':
    # 使用fire库为Calculator类生成命令行接口
    fire.Fire(Calculator)

"""
python fire_demo_2.py add 1 2
# 调用add方法，将1和2相加，输出结果3
python fire_demo_2.py multiply 2 3
python fire_demo_2.py multiply --a=2 --b=3
# 调用multiply方法，将2和3相乘，输出结果6
python fire_demo_2.py minus 2 3
# 调用minus方法，从2中减去3，输出结果-1
"""
