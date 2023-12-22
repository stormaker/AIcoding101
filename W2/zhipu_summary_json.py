# book_summary.py
import fire
import requests
import configparser
import zhipuai
import json
from datetime import datetime

# 读取配置文件以获取API密钥
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['DOUBAN_API']
zhipuai.api_key = config['API']['zhipuai.api_key']


class DouBanBookUtil:
    @staticmethod
    def _post(url, data):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edge/115.0.1901.203"
        }
        response = requests.post(url, data=data, headers=headers)
        text = response.json()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{timestamp}.json"
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(text, f, ensure_ascii=False, indent=4)
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
            #print(book_brief)
            with open(f"{book_name}-简介.txt", 'w', encoding='utf-8') as file:
                 file.write(book_brief)
            return book_brief
        else:
            print("No book found with the given name.")


def zhipu_prompt(book_brief):
    with open("redbook_prompt.txt", "r", encoding='utf-8') as f:
        redbook_prompt = f.read()
        response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user", "content": redbook_prompt + "以下是书籍信息" + book_brief}],
            top_p=0.7,
            temperature=0.9,
        )
        return response


def book_summary_cli(book_name):
    util = DouBanBookUtil()
    book_summary = util.get_book_summary_by_name(book_name)
    print(book_summary)
    zhipu_response = zhipu_prompt(book_summary)
    redbook_str = zhipu_response['data']['choices'][0]['content']
    redbook_str = redbook_str.replace(r"\n", "\n")
    redbook_str = redbook_str.replace(r'\"',"" )
    redbook_str = redbook_str[1:-1].strip()
    print(redbook_str)
    # with open(f"{book_name}-小红书文案.txt", 'w', encoding='utf-8') as file:
    #     file.write(redbook_str)

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
