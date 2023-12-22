import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import time


def crawl_text_and_images(url):
    # 发送HTTP请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 创建一个字典来存储爬取的数据
    data = {
        'url': url,
        'text': [],
        'images': []
    }

    # 抓取所有文字内容，例如段落
    text_content = soup.find_all('p')
    for paragraph in text_content:
        text = paragraph.get_text(strip=True)
        if text:  # 添加非空文本
            data['text'].append(text)

    # 抓取所有图片链接
    images = soup.find_all('img')
    for image in images:
        img_src = image.get('src')
        if img_src:
            # 构建完整的图片链接
            full_img_url = urljoin(url, img_src)
            data['images'].append(full_img_url)

    # 生成文件名：公众号+时间戳.json
    timestamp = int(time.time())
    output_filename = f"公众号_{timestamp}.json"

    # 将数据写入JSON文件
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Data has been written to {output_filename}")


# 指定要爬取的网页
url_to_crawl = 'https://mp.weixin.qq.com/s/nZ8ScL-k2CzKMsDyYIO_FA'

# 调用函数
crawl_text_and_images(url_to_crawl)
