import os
from dotenv import load_dotenv
load_dotenv()

# 用getenv()方法读取.env文件中的变量
douban_api = os.getenv('douban_api')
zhipuai_api = os.getenv('zhipuai_api')
coding = os.getenv('coding_api')
openai_api = os.getenv('openai_api')

print(f"{openai_api}\n")

# 输出变量值
print(douban_api)
print(zhipuai_api)
print(coding)
