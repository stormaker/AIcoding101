import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
import json


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
    output_file = f"{author}-{formatted_dt}.json"

    # 构建要保存的数据字典
    data = {
        "url": url,
        "author": author,
        "title": title,
        "text_content": [],
        "image_links": []
    }

    # 抓取所有文字内容，例如段落，并添加到数据字典中
    text_content = soup.find_all('p')
    for paragraph in text_content:
        text = paragraph.get_text(strip=True)
        if text:  # 添加非空文本
            data['text_content'].append(text)

    # 抓取所有图片链接，并添加到数据字典中
    img_tags = soup.find_all('img', attrs={'class': 'rich_pages wxw-img'})
    for img_tag in img_tags:
        data_src = img_tag.get('data-src')
        if data_src:
            data["image_links"].append(data_src)

    # 将数据字典保存为JSON文件
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# 读取urls.txt文件中的URL列表
with open('urls.txt', 'r') as file:
    urls = file.readlines()

# 遍历URL列表，逐个进行抓取和保存
for url in urls:
    url = url.strip()  # 去除换行符和空格
    crawl_text_and_images(url)
