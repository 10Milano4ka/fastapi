from fastapi import FastAPI, Response,Path, Cookie
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse, PlainTextResponse
from datetime import datetime

app = FastAPI()


@app.get("/")
async def main ():
    return {"мяу": "йоу мяумяумяу"}


@app.get("/json")
async def main ():
    return JSONResponse({"и есть тоже": "я хочу спать"})

@app.get("/html")
async def main ():
    return HTMLResponse("<h1>пишу текст для вас эм да пон да лол кек чебурек коля демон</h1>")

@app.get("/text")
async def main ():
    return PlainTextResponse("чо писать эм бож чел я устала ходить в школу =( ")

@app.get("/file")
async def main ():
    return FileResponse("index.html")

@app.get("/filedownload")
async def main ():
    return FileResponse("index.html", filename = "index.html", media_type="application/octet-stream")

@app.get("/user/{id}/{name}")
async def main (id: int,name: str):
    return {"userid": id, "username": name} 

@app.get("/age/{age}/{nickname}")
async def main (age: int = Path(ge=12,lt=21),nickname: str = Path(min_length=2,max_length=10)):
    return {"age": age,"nickname": nickname} 

# @app.get("/url/{url}")
# async def main (url:str=Path(regex="\d{12}")):
#     return {"url": url}
 
@app.get("/url/{url}")
async def main (url:str=Path(regex="8\d{10}")):
    return {"url": url} 

@app.get("/cookie")
async def main(response: Response) :
    now = datetime.now()
    response.set_cookie(key="last_visit", value=now)
    return {"message": "cokkie установлен"}   

@app.get("/getcookie")
async def main (last_visit = Cookie()):
    return {"last_visit": last_visit} 