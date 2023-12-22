import requests
from bs4 import BeautifulSoup
import re
import time
import datetime


def crawl_text_and_images(url):
    # 发送HTTP请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {url}")
        return

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('meta', attrs={'property': 'og:title'}).get('content')
    profile_nickname = soup.find('strong', class_='profile_nickname')
    author = profile_nickname.get_text()

    timestamp = int(time.time())
    dt = datetime.datetime.fromtimestamp(timestamp)
    formatted_dt = dt.strftime("%Y-%m-%d-%H%M")
    output_file = f"{author}-{formatted_dt}.md"

    # 打开文件以写入爬取的内容
    with open(output_file, 'w', encoding='utf-8') as file:
        # 写入URL
        file.write(f"URL: {url}\n")
        file.write(f"Author: {author}\n")
        file.write(f"Title: {title}\n\n")

        # 抓取所有文字内容，例如段落，并写入文件
        text_content = soup.find_all('p')
        for paragraph in text_content:
            text = paragraph.get_text()
            file.write(text + "\n")

        # 添加一个分隔符
        file.write("\n---\n\n")

        # 抓取所有图片链接，并写入文件
        img_tags = soup.find_all('img', attrs={'class': 'rich_pages wxw-img'})
        for img_tag in img_tags:
            data_src = img_tag.get('data-src')
            if data_src:
                file.write(data_src + "\n")

    # 调用函数去除多余的空行
    normalize_newlines(output_file)


def normalize_newlines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式替换多个连续换行为单个换行
    normalized_content = re.sub(r'\n{2,}', '\n\n', content)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(normalized_content)


# 读取urls.txt文件中的URL列表
with open('urls.txt', 'r') as file:
    urls = file.readlines()

# 遍历URL列表，逐个进行抓取和保存
for url in urls:
    url = url.strip()  # 去除换行符和空格
    crawl_text_and_images(url)
