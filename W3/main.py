import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# BaseModel定义了POST请求的数据模型


class Item(BaseModel):
    id: int
    name: str

# 根路由处理GET请求，返回默认消息


@app.get("/")
async def root():
    return {"message": "Hello World"}

# 个性化问候路由处理GET请求，动态捕获名字并返回个性化问候


@app.get("/name/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# 处理POST请求，接收id和name参数，并返回它们


@app.post("/api/create")
async def create_item(item: Item):
    return {"id": item.id, "name": item.name}

# 主程序入口，启动uvicorn服务器
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
