from fastapi import FastAPI
from routes.hello import router as hello_router
from routes.todo import router as todo_router



app=FastAPI() #fastapi 서버 생성

@app.get("/") # http://127.0.0.1:8000/ 접속시 호출되는 함수
async def welcome() -> dict: # {key:value} 형태의 dict 반환 json 타입
    return {
        "message": "GET:: Hello FastAPI!"
    }

@app.post("/") # http://127.0.0.1:8000/ 접속시 호출되는 함수
async def welcome() -> dict: # {key:value} 형태의 dict 반환 json 타입
    return {
        "message": "POST:: Hello FastAPI!"
    }


app.include_router(hello_router) # hello.py 라우터 등록
app.include_router(todo_router) # todo.py 라우터 등록