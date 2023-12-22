# W2_adv_task02_extended.py
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
# print(zhipuai.api_key)
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
        params = {"q": name, "apikey": douban_api}
        data = self._post(url, params)
        books = data.get("books")
        if books:
            return books[0].get("id")
        return None

    def get_book_info(self, book_id):
        url = f"https://api.douban.com/v2/book/{book_id}"
        data = self._post(url, {"apikey": douban_api})
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
            # 创建书籍简介字符串
            book_brief = f"Book Name: {book_name}\n\nAuthors: {', '.join(authors)}\n\nISBN: {book_isbn}\n\nSummary:\n{book_summary}"
            # 保存书籍简介到文件
            with open(f"{book_name}-简介.txt", 'w', encoding='utf-8') as file:
                file.write(book_brief)
            return book_brief
        else:
            print("No book found with the given name.")
            return None


def zhipu_prompt(book_brief):
    if book_brief is None:
        return "No book brief available to generate the prompt."
    with open("redbook_prompt.txt", "r", encoding='utf-8') as f:
        redbook_prompt = f.read()
        response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user",
                     "content": redbook_prompt + "以下是书籍信息" + book_brief}],
            top_p=0.7,
            temperature=0.9,
        )
        return response


def book_promotions_cli(book_names):
    book_names = book_names.split("-")  # 使用'-'作为书名分隔符
    util = DouBanBookUtil()

    for book_name in book_names:
        book_summary = util.get_book_summary_by_name(book_name.strip())
        if book_summary:
            print(book_summary)
            zhipu_response = zhipu_prompt(book_summary)
            redbook_str = zhipu_response['data']['choices'][0]['content']
            with open(f"{book_name}-origin.txt", 'w', encoding='utf-8') as file:
                file.write(redbook_str)
            redbook_str = redbook_str.replace(r'\n', "\n")
            redbook_str = redbook_str.replace(r'\"', "")
            redbook_str = redbook_str[1:-1].strip()
            print(redbook_str)
            print("-" * 60)  # 输出分隔线以区分不同书籍的推广文案

            # Save the promotional text to a file
            with open(f"{book_name}-小红书文案.txt", 'w', encoding='utf-8') as file:
                file.write(redbook_str)


if __name__ == '__main__':
    # 使用 fire 来创建一个命令行界面
    fire.Fire(book_promotions_cli)
