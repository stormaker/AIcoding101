import zhipuai
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 读取环境变量中的zhipuai_api_key，需要单独新建.env的文件存储这个值
zhipuai.api_key = os.getenv('ZHIPUAI_API_KEY')
input_text = input("请输入你要问的问题")
response = zhipuai.model_api.sse_invoke(
    model="chatglm_turbo",
    prompt=[{"role": "user", "content": input_text}],
    temperature=0.9,
    top_p=0.7,
    incremental=True
)

for event in response.events():
    if event.event == "add":
        print(event.data, end="")
    elif event.event == "error" or event.event == "interrupted":
        print(event.data, end="")
    # elif event.event == "finish":
    #     print(event.data)
    #     print(event.meta, end="")
    else:
        print(event.data, end="")
