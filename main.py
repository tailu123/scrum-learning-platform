from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import uvicorn
from termcolor import colored
import os

app = FastAPI()

# 挂载静态文件
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        print(colored("访问主页", "cyan"))
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        print(colored(f"Error reading index.html: {str(e)}", "red"))
        return "Error loading page"

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("images/favicon.ico")

if __name__ == "__main__":
    print(colored("Starting Scrum Guide website server...", "cyan"))
    try:
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    except Exception as e:
        print(colored(f"Server error: {str(e)}", "red")) 