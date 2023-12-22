from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path

# 初始化 FastAPI 应用、模板和静态文件
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 文件上传路径
UPLOAD_DIR = "upload"
Path(UPLOAD_DIR).mkdir(exist_ok=True)

DOWNLOAD_DIR = "download"
Path(DOWNLOAD_DIR).mkdir(exist_ok=True)

# 加载环境变量
load_dotenv()
openai_api = os.getenv("OPENAI_API_KEY")


# WebSocket连接管理器
class ConnectionManager:
	def __init__(self):
		self.active_connections: List[WebSocket] = []

	async def connect(self, websocket: WebSocket):
		await websocket.accept()
		self.active_connections.append(websocket)

	async def disconnect(self, websocket: WebSocket):
		self.active_connections.remove(websocket)

	async def broadcast(self, message: str):
		for connection in self.active_connections:
			await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
	await manager.connect(websocket)
	try:
		while True:
			await websocket.receive_text()
	except WebSocketDisconnect:
		await manager.disconnect(websocket)


@app.get("/")
async def get(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
	file_location = f"{UPLOAD_DIR}/{file.filename}"
	with open(file_location, "wb+") as file_object:
		file_object.write(file.file.read())
	# 开始处理文件
	await process_file(file_location)
	return {"info": "File uploaded successfully", "filename": file.filename}


@app.get("/download/{filename}")
async def download_file(filename: str):
    """
    通过这个端点可以下载处理后的文件。
    :param filename: 请求下载的文件名
    :return: FileResponse 对象
    """
    file_path = os.path.join(DOWNLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename)
    else:
        return {"error": "File not found"}


def summarize_text(text):
	client = OpenAI()
	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role": "assistant",
				"content": f"请将我发送的语音稿整理为正式的书面语，要求"
						   f"-保留对话中的每一个细节，不改变原文含义；"
						   f"-尽可能地保留原话的用词、话语风格；"
						   f"-请修改错别字，符合中文语法规范。"
						   f"-去掉说话人和时间戳。:{text}"
			}
		],
		temperature=0,
		max_tokens=2000,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)
	return response.choices[0].message.content


async def process_file(file_path):
	# 读取文件
	with open(file_path, "r", encoding='utf-8') as f:
		text = f.read()

	# 分割文本
	text_splitter = RecursiveCharacterTextSplitter(chunk_size=1100, chunk_overlap=20, length_function=len,
												   is_separator_regex=False)
	chunks = text_splitter.split_text(text)
	filename_without_extension = os.path.splitext(os.path.basename(file_path))[0]

	# 初始化进度
	total_chunks = len(chunks)
	processed_chunks = 0

	# 处理每个文本块
	summaries = []
	for i, chunk in enumerate(chunks):
		summary = summarize_text(chunk)
		summaries.append(summary)
		chunk_file_path = os.path.join(DOWNLOAD_DIR, f'{filename_without_extension}_summary_chunk_{i + 1}.txt')
		with open(chunk_file_path, 'w', encoding='utf-8') as file:
			file.write(summary)

	# 更新进度
	total_chunks = len(chunks)
	for i, chunk in enumerate(chunks):
		# ...[处理每个块的代码]...

		# 更新进度
		progress = int((i + 1) / total_chunks * 100)  # i + 1，因为i从0开始
		await manager.broadcast(f'{{"type": "progress", "value": {progress}}}')

	output_file_path = os.path.join(DOWNLOAD_DIR, f'{filename_without_extension}_summary_output.txt')
	with open(output_file_path, 'w', encoding='utf-8') as file:
		for i, summary in enumerate(summaries):
			# file.write(f'Summary Chunk {i+1}:\n\n')
			file.write(summary + '\n\n')
	# 可以将处理结果保存或进一步处理
	file_name_for_download = f'{filename_without_extension}_summary_output.txt'
	await manager.broadcast(f'{{"type": "file_ready", "filename": "{file_name_for_download}"}}')





if __name__ == "__main__":
	import uvicorn

	uvicorn.run("main:app", host="127.0.0.1", reload=True, port=80, log_level="info")