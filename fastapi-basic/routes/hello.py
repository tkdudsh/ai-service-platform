from fastapi import APIRouter
from pydantic import BaseModel

hello_router = APIRouter() # fastapi 라우터 생성

class Person(BaseModel):
    name:str
    age:int

@hello_router.get("/hello") # http://127.0.0.1:8000/ 접속시 호출되는 함수
async def sayhello() -> dict: # {key:value} 형태의 dict 반환 json 타입
    return {
        "message": "Hello FastAPI!22"
    }

@hello_router.post("/hello") # http://127.0.0.1:8000/ 접속시 호출되는 함수
async def sayhello(person: Person) -> dict: # {key:value} 형태의 dict 반환 json 타입
    return {
        "message": f"Hello, {person.name}! You are {person.age} years old."
    }

