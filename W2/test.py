import requests
import fire

import os
from dotenv import load_dotenv

load_dotenv()
douban_api = os.getenv('douban_api')


class DoubanBookUtil:
    def __init__(self):
        self.douban_api = douban_api
        self.base_url = "https://api.douban.com/v2/book/"

    def _post(self, url, params=None):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        response = requests.post(
            url,
            data={
                'apikey': self.douban_api},
            params=params,
            headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_book_id_by_book_name(self, book_name):
        url = self.base_url + "search"
        result = self._post(url, params={'q': book_name, 'count': 1})
        try:
            return result["books"][0]['id']
        except (KeyError, TypeError, IndexError):
            return None

    def get_book_info(self, book_id):
        url = self.base_url + str(book_id)
        book_info = self._post(url)
        return book_info

    def get_book_summary(self, book_name):
        book_id = self.get_book_id_by_book_name(book_name)
        if book_id:
            book_info = self.get_book_info(book_id)
            try:
                book_name = book_info['title']
                book_isbn = book_info['isbn13']
                book_author = ', '.join(book_info['author'])
                book_summary = book_info['summary']
                book_brief = f"book_name:{book_name}\nbook_isbn:{book_isbn}\nbook_author:{book_author}\nbook_summary:{book_summary}"
                # print(book_brief)
                return book_brief
            except KeyError:
                print("Incomplete book information.")
                return None
        else:
            print("Book not found")
            return None


def book_summary_cli(book_name):
    util = DoubanBookUtil()
    book_summary = util.get_book_summary(book_name)
    if book_summary:
        print(book_summary)


if __name__ == "__main__":
    fire.Fire(book_summary_cli)
