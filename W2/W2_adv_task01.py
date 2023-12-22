import fire
import requests
import os
from dotenv import load_dotenv

# 该函数会查找项目的根目录中的.env文件，并自动加载变量
load_dotenv()

# 读取配置文件以获取API密钥
douban_api = os.getenv('DOUBAN_API')
# print(douban_api)

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
            return [book.get("id") for book in books]
        return []

    def get_book_info(self, book_id):
        url = f"https://api.douban.com/v2/book/{book_id}"
        data = self._post(url, {"apikey": douban_api})
        return data

    def get_multiple_book_summaries_by_name(self, names):
        summaries = []
        for name in names:
            book_ids = self.get_book_id_by_name(name)
            if book_ids:
                # Assuming we only want the first result per book name
                for book_id in book_ids[:1]:
                    book_info = self.get_book_info(book_id)
                    book_name = book_info.get('title')
                    book_isbn = book_info.get('isbn13')
                    authors = book_info.get('author')
                    book_summary = book_info.get('summary')
                    book_brief = f"Book Name: {book_name}\n\nAuthors: {', '.join(authors) if authors else 'No authors listed'}\n\nISBN: {book_isbn}\n\nSummary:\n{book_summary if book_summary else 'No summary found.'}\n{'-'*40}\n"
                    summaries.append(book_brief)
            else:
                summaries.append(
                    f"No book found with the name: {name}\n{'-'*40}\n")
        return "\n".join(summaries)


def book_summary_cli(book_name):
    util = DouBanBookUtil()
    book_names = book_name.split("-")  # Split book names using '-'
    book_summaries = util.get_multiple_book_summaries_by_name(book_names)
    with open(f"{book_name}-简介.txt", 'w', encoding='utf-8') as file:
        file.write(book_summaries)
    print(book_summaries)


if __name__ == '__main__':
    # 使用 fire 来创建一个命令行界面
    fire.Fire(book_summary_cli)
