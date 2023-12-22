# fire_demo_1.py
# 导入fire库
import fire

# 定义一个函数，该函数有一个默认参数name，其默认值为"World"
# 可变参数 kwargs 表示还可以接受其他任意数量的参数
# 该函数返回一个问候语
def hello(name="World", *kwargs):
    return f"Hello {name} {' '.join(kwargs)}!"

# 这个判断用来确定代码是直接运行还是被其他模块导入
# 如果是直接运行，则执行以下代码
if __name__ == '__main__':
    # 使用fire库为hello函数生成命令行接口
    fire.Fire(hello)

"""
需要 pip install fire
python fire_demo_1.py --help
这将打印由 fire 为 hello 函数生成的帮助消息。它会显示如何使用该函数，它的参数以及它们的默认值。
python fire_demo_1.py Iris
python fire_demo_1.py --name=Iris
这将以 "Iris" 为 name 参数的值调用 hello 函数。因此，它会打印"Hello Iris!"。
python fire_demo_1.py Iris ABC
这条命令会将 Kiki 作为 name 参数传递，并传递一个额外的参数 ABC。结果会输出 "Hello Iris ABC!"。
"""
