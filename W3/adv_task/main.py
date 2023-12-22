from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
import zhipuai  # 引入智普AI库
from pydantic import BaseModel  # 用于创建数据模型
from dotenv import load_dotenv  # 用于加载.env文件中的环境变量
import os  # 用于操作系统功能，比如环境变量

# 加载环境变量
load_dotenv()

# 读取环境变量中的zhipuai_api_key，需要单独新建.env的文件存储这个值
zhipuai.api_key = os.getenv('ZHIPUAI_API_KEY')

# 创建FastAPI应用实例
app = FastAPI()

# 使用Pydantic定义数据模型，这里定义了一个Item类，有一个prompt字段，类型是字符串或None，默认为空字符串


class Item(BaseModel):
    prompt: str | None = ''


# 设置Jinja2模板文件的存储目录
templates = Jinja2Templates(directory="templates")


# 将静态文件目录挂载到应用，使得可以通过/static/路径访问
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # 根目录的GET请求响应，返回渲染后的index.html文件
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/api/generate')
async def generate(item: Item):
    # 定义一个生成器，用于智普AI API的流式响应
    def stream():
        # 调用智普AI的API，发送请求并获取流式响应
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user", "content": f"你好，请按照以下提供的内容{item.prompt}，生成小红书文案，要求包括三部分：标题、内容和标签，记得分行，并且添加小红书用户特有emoji风"}],
            top_p=0.7,
            temperature=0.9,
        )
        # 遍历流式响应中的事件，并逐个产出数据
        for event in response.events():
            yield event.data

    # 创建流式响应对象，当API被调用时返回数据流
    return StreamingResponse(stream())


# 如果是直接执行这个文件，则启动服务，监听本地1234端口
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8000, log_level="info")
