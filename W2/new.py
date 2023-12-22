import fire
import requests
import os
from dotenv import load_dotenv

# Load the .env file where the DOUBAN_API_KEY is stored
load_dotenv()
douban_api_key = os.getenv('douban_api')
# print(douban_api_key)

class DouBanBookUtil:

	@staticmethod
	def _post(url, data):
		"""Send a POST request to the specified URL."""
		headers = {
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edge/115.0.1901.203"
		}
		response = requests.post(url, data=data, headers=headers)
		return response.json()

	@staticmethod
	def get_book_id_by_name(book_name):
		"""Get book ID by name from the DouBan API."""
		url = f'https://api.douban.com/v2/book/search?q={book_name}'
		params = {"q": book_name, "apikey": douban_api_key,"count": 1}
		response = DouBanBookUtil._post(url, data=params)
		books = response.get('books', [])
		return [book['id']for book in books] if books else []

	@staticmethod
	def get_book_info(book_id):
		"""Get book info by ID from the DouBan API."""
		url = f'https://api.douban.com/v2/book/{book_id}'
		return DouBanBookUtil._post(url, data={"apikey": douban_api_key})

	@staticmethod
	def get_multiple_book_summaries_by_name(book_names):
		"""Get multiple book summaries by names."""
		summaries = []
		for name in book_names:
			ids = DouBanBookUtil.get_book_id_by_name(name)
			for book_id in ids:
				info = DouBanBookUtil.get_book_info(book_id)
				summaries.append(info.get('summary', 'No summary available.'))
		return summaries


def book_summary_cli(book_name):
	"""CLI function to write and print book summaries."""
	book_names = book_name.split('-')
	summaries = DouBanBookUtil.get_multiple_book_summaries_by_name(book_names)
	for summary in summaries:
		print(summary)
	# You could also write to a file here if needed.


if __name__ == '__main__':
	fire.Fire(book_summary_cli)