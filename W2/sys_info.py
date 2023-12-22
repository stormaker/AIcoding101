# sys_info.py
# 使用 pip 安装 psutil 库
# pip install psutil
import psutil  # 导入psutil库，用于获取系统信息

def cup_info():
    # 获取CPU信息

    # 获取 CPU 物理核心数量
    cpu_count = psutil.cpu_count(logical=False)
    # 获取逻辑核心数量
    logical_cpu_count = psutil.cpu_count(logical=True)

    # 获取CPU使用率，每秒更新一次
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    # 打印CPU信息
    print(f"物理CPU核心数量: {cpu_count}")
    print(f"逻辑CPU核心数量: {logical_cpu_count}")
    for i, usage in enumerate(cpu_usage):
        print(f"CPU核心 {i + 1} 使用率: {usage}%")

def memory_info():
    # 获取内存信息

    info = psutil.virtual_memory()

    # 打印内存信息
    print(f"总内存容量: {info.total / (1024 ** 3):.2f} GB")
    print(f"已使用内存: {info.used / (1024 ** 3):.2f} GB")
    print(f"可用内存: {info.available / (1024 ** 3):.2f} GB")
    print(f"内存使用率: {info.percent}%")

def main():
    # 主函数：调用以上两个函数获取并打印CPU和内存信息
    cup_info()
    memory_info()

# 当直接运行此脚本时，执行main()函数
if __name__ == "__main__":
    main()