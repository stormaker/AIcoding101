import json
import requests
import time
import random
from pathlib import Path


# 读取JSON文件并解析图片链接
def load_image_links(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data.get('image_links', [])


# 下载并保存图片
def download_images(image_links):
    for index, url in enumerate(image_links):
        try:
            response = requests.get(url)
            response.raise_for_status()  # 确保请求成功

            # 保存图片
            image_path = f'image_{index}.jpg'
            with open(image_path, 'wb') as file:
                file.write(response.content)

            print(f'Downloaded image {index + 1}/{len(image_links)}')

        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # HTTP错误
        except Exception as err:
            print(f'An error occurred: {err}')  # 其他错误

        # 暂停随机时间
        time_to_sleep = random.randint(1, 3)
        print(f'Pausing for {time_to_sleep} seconds...')
        time.sleep(time_to_sleep)


# 主程序入口
def main(json_file):
    image_links = load_image_links(json_file)
    download_images(image_links)


# 运行程序
if __name__ == '__main__':
    json_file = '拱宸-2023-11-14-0129.json'  # 指定JSON文件路径
    main(json_file)
