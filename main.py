from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from termcolor import colored
import os

app = FastAPI()

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 确保目录存在
for directory in ['js', 'css', 'images']:
    os.makedirs(directory, exist_ok=True)

try:
    # 挂载静态文件
    app.mount("/js", StaticFiles(directory="js"), name="js")
    app.mount("/css", StaticFiles(directory="css"), name="css")
    app.mount("/images", StaticFiles(directory="images"), name="images")
except Exception as e:
    print(colored(f"Error mounting static files: {str(e)}", "red"))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        print(colored("访问主页", "cyan"))
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        print(colored(f"Error reading index.html: {str(e)}", "red"))
        return f"""
        <html>
            <head>
                <title>Error</title>
            </head>
            <body>
                <h1>Error loading page</h1>
                <p>{str(e)}</p>
            </body>
        </html>
        """

@app.get("/favicon.ico")
async def favicon():
    if os.path.exists("images/favicon.ico"):
        return FileResponse("images/favicon.ico")
    return None

# Vercel需要的app实例
app = app

if __name__ == "__main__":
    print(colored("Starting Scrum Guide website server...", "cyan"))
    try:
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    except Exception as e:
        print(colored(f"Server error: {str(e)}", "red")) 