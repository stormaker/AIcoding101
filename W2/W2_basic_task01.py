# book_summary.py
import fire
import requests
import os
import zhipuai

from dotenv import load_dotenv

# 该函数会查找项目的根目录中的.env文件，并自动加载变量
load_dotenv()

# 读取配置文件以获取API密钥
douban_api = os.getenv('DOUBAN_API')
zhipuai.api_key = os.getenv('ZHIPUAI_API_KEY')

class DouBanBookUtil:
    @staticmethod
    def _post(url, data):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edge/115.0.1901.203"
        }
        response = requests.post(url, data=data, headers=headers)
        return response.json()

    def get_book_id_by_name(self, name):
        url = f"https://api.douban.com/v2/book/search"
        params = {"q": name, "apikey": api_key}
        data = self._post(url, params)
        books = data.get("books")
        if books:
            return books[0].get("id")
        return None

    def get_book_info(self, book_id):
        url = f"https://api.douban.com/v2/book/{book_id}"
        data = self._post(url, {"apikey": api_key})
        return data

    def get_book_summary_by_name(self, name):
        book_id = self.get_book_id_by_name(name)
        if book_id:
            book_info = self.get_book_info(book_id)
            # 收集所需信息
            book_name = book_info.get('title')
            book_isbn = book_info.get('isbn13')
            authors = book_info.get('author')
            book_summary = book_info.get('summary')
            # 打印所需信息
            # print(f"Book Name: {book_name}")
            # print(f"Book ID: {book_id}")
            # print(f"ISBN: {book_isbn}")
            # print("Authors: " + ", ".join(authors) if authors else "No authors listed")
            # print("Summary:\n" + book_summary if book_summary else "No summary found.")
            book_brief: str = f"Book Name: {book_name}\n\nAuthors:{authors}\n\nISBN: {book_isbn}\n\nSummary:\n{book_summary}"
            # print(book_brief)
            with open(f"{book_name}-简介.txt", 'w', encoding='utf-8') as file:
                file.write(book_brief)
            return book_brief
        else:
            print("No book found with the given name.")


def book_summary_cli(book_name):
    util = DouBanBookUtil()
    book_summary = util.get_book_summary_by_name(book_name)
    print(book_summary)


if __name__ == '__main__':
    # 使用 fire 来创建一个命令行界面
    fire.Fire(book_summary_cli)

"""
安装依赖：
pip install requests fire

运行：
python book_summary.py --book_name "自私的基因"
此命令将使用提供的书名获取书籍摘要及其他信息
"""
