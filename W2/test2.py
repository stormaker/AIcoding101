import fire
import requests

import os
from dotenv import load_dotenv
load_dotenv()

# 使用os库获取环境变量
douban_api = os.getenv('douban_api')


class DouBanBookUtil:
    def __init__(self):
        self.douban_api = douban_api

    def _post(self, url, params=None):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        try:
            response = requests.post(url, data={'apikey': self.douban_api}, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Error Connecting: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout Error: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Error: {req_err}")
        return None

    def get_book_id_by_name(self, name):
        url = f"https://api.douban.com/v2/book/search"
        params = {"q": name, "apikey": self.douban_api}
        data = self._post(url, params)
        books = data.get("books") if data else []
        book_ids: list = [book.get("id") for book in books]
        return book_ids

    def get_book_info(self, book_id):
        url = f"https://api.douban.com/v2/book/{book_id}"
        data = self._post(url, {"apikey": self.douban_api})
        return data

    def get_multiple_book_summaries_by_name(self, names):
        summaries = []
        for name in names:
            book_ids = self.get_book_id_by_name(name)
            for book_id in book_ids[:1]:  # 保证每个名称只获取一个书籍的简介
                book_info = self.get_book_info(book_id)
                if book_info:
                    book_name = book_info.get('title')
                    book_isbn = book_info.get('isbn13')
                    authors = book_info.get('author')
                    book_summary = book_info.get('summary')
                    book_brief = f"Book Name: {book_name}\n\nAuthors: {', '.join(authors) if authors else 'No authors listed'}\n\nISBN: {book_isbn}\n\nSummary:\n{book_summary if book_summary else 'No summary found.'}\n{'-' * 40}\n"
                    summaries.append(book_brief)
                else:
                    summaries.append(f"No book found with the name: {name}\n{'-' * 40}\n")
        return "\n".join(summaries)


def book_summary_cli(book_names):
    util = DouBanBookUtil()
    book_names_list = book_names.split("-")  # 使用 '-' 分隔书名
    # print(book_names_list)
    book_summaries = util.get_multiple_book_summaries_by_name(book_names_list)
    # with open(f"{book_names}-简介.txt", 'w', encoding='utf-8') as file:
    #     file.write(book_summaries)
    print(book_summaries)


if __name__ == '__main__':
    fire.Fire(book_summary_cli)
