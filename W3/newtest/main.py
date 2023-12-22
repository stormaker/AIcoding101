from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn
import zhipuai
import os
from dotenv import load_dotenv
from pydantic import BaseModel

# 加载环境变量
load_dotenv()

# 读取环境变量中的zhipuai_api_key，需要单独新建.env的文件存储这个值
zhipuai.api_key = os.getenv('ZHIPUAI_API_KEY')
app = FastAPI()


class Item(BaseModel):
    prompt: str | None = ''


# 设置 templates 和 static 文件夹的路径
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/generate")
async def generate(item: Item):
    def stream():
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_turbo",
            prompt=[
                {"role": "user",
                 "content": f"请对以下产品```{item.prompt}```，生成生成小红书文案，要求包括三部分：标题、内容和标签"}
            ],
            temperature=0.7,
            top_p=0.95,
        )

        for event in response.events():
            yield event.data

    return StreamingResponse(stream())


# 如果是直接执行这个文件，则启动服务，监听本地1234端口
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8000,
        log_level="info")