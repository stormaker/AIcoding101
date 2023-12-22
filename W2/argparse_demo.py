# argparse_demo.py
# https://docs.python.org/3.11/library/argparse.html
import argparse
from fire_demo_2 import Calculator


def parser_args():
    # 创建一个命令行参数解析器
    parser = argparse.ArgumentParser()
    # 添加命令行参数，用于指定要执行的操作（add/minus/multiply/double）
    parser.add_argument("action", help="add/minus/multiply/double")
    # 添加命令行参数，用于指定第一个数字
    parser.add_argument("x", type=int, help="the first number")
    # 添加命令行参数，用于指定第二个数字（可选），默认值为0
    parser.add_argument("y", nargs="?", type=int, help="the second number", default=0)
    # 解析命令行参数
    args = parser.parse_args()
    # 获取操作类型
    return args


def action(args):
    # 创建一个 Calculator 对象
    ctl = Calculator()
    action = args.action
    # 根据操作类型决定要传递给计算器的数字参数
    numbers = [args.x, args.y] if action != "double" else [args.x]
    # 调用 Calculator 对象的相应方法执行计算，并获取结果
    res = getattr(ctl, action)(*numbers)
    # 打印计算结果
    print(res)


def main():
    args = parser_args()
    action(args=args)


if __name__ == "__main__":
    main()

"""
python argparse_demo.py add 1 2
# 调用add方法，将1和2相加，输出结果3
python argparse_demo.py multiply 2 3
# 调用multiply方法，将2和3相乘，输出结果6
python argparse_demo.py minus 2 3
# 调用minus方法，从2中减去3，输出结果-1
"""