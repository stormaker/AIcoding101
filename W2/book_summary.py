# book_summary.py
# 导入fire库，用于快速地创建命令行接口
# https://github.com/google/python-fire
import fire
# requests 用于HTTP请求
import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['DOUBAN_API']

# 定义一个函数，通过ISBN号从豆瓣API获取书籍摘要
def get_book_summary(isbn) -> str:
    # https://feizhaojun.com/?p=3813
    # https://www.doubanapi.com/
    # 注意：API密钥不应该直接放在代码中，豆瓣的 api 平台现已关闭，这里找的是网友找到的可用的
    # 根据提供的ISBN构建请求的URL
    url = f"https://api.douban.com/v2/book/isbn/{isbn}"
    # 使用requests库发起HTTP请求，设置请求头来模拟正常浏览器行为
    # User-Agent 告诉服务器发起请求的客户端的软件类型和版本
    # 不设的话 requests 库默认会发送 requests 加版本号，然后豆瓣的 api 会返回 b''
    response = requests.post(url,
                             data={"apikey": api_key},
                             headers={
                                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"})
    # 解析响应的JSON数据
    data = response.json()
    # 返回书籍摘要
    #return data.get("summary")
    return data
def book_summary(isbn: str = '9787521748536'):
    data = get_book_summary(isbn)
    print(data)

# 如果脚本作为主程序运行，那么获取指定ISBN的书籍摘要并打印
if __name__ == '__main__':
    fire.Fire(book_summary)

"""
需要 pip install requests
python book_summary.py --isbn 9787521748536
此命令将使用提供的ISBN获取书籍摘要
"""